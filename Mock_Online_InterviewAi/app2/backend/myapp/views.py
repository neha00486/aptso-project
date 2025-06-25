from django.shortcuts import render
from django.conf import settings
import os
import re
import random
import datetime
import wave
import contextlib
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app2.backend.myapp.gem_test.get_resume import get_resume
from app2.backend.myapp.gem_test.t2 import get_chat, stream_complete_sentences # Keeping Gemini
from app2.backend.myapp.tts_test.t5 import GTTSTTSPlayer
from app2.backend.myapp.speach_rec_test.rt_3.t1 import set_ear, Listen
# REMOVED: from app2.backend.myapp.str_comp_test.t5 import set_sentance_complete, is_complete
from app2.backend.myapp.non_verbal.nv import set_non_verbal, evaluate_posture
from app2.backend.myapp.filler_count.filler_count import count_filler_words
from app2.backend.myapp.evaluation_score import evaluation_score
import time
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import cv2
import mediapipe as mp
import json
import pathlib
import requests # Keep for Gemini if t2.py uses it (though genai SDK usually handles it)
from google import genai # Keep for Gemini
from markdown import Markdown # Keep for Gemini if t2.py uses it
import tempfile # Keep if t2.py uses it
import uuid # Keep if t2.py uses it
from google.genai import types # Keep for Gemini


stop_nv = False
non_verbal_data = {
    "good_posture": 0,
    "unclear_posture": 0,
    "good_eye_contact": 0,
    "no_eye_contact": 0,
}
playAudio = "false"
change_flag = 'false'

def lipsync_start():
    global playAudio, change_flag
    frontend_base_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "frontend", "public", "audios")
    json_file_path = os.path.join(frontend_base_dir, "output.json")
    data = None
    try:
        with open(json_file_path, 'r') as f:
            data = json.load(f)
        duration = data['metadata']['duration']
        print(f"Duration from JSON: {duration}")
        playAudio = "true"
        change_flag = 'true'
        time.sleep(0.6)
        change_flag = 'false'
        time.sleep(duration)
        playAudio = "false"
        change_flag = 'true'
        time.sleep(0.6)
        change_flag = 'false'
    except FileNotFoundError:
        print(f"Error: Lipsync JSON file not found at {json_file_path}. Skipping lipsync.")
    except KeyError:
        print(f"Error: 'metadata' or 'duration' key not found in {json_file_path}. Skipping lipsync.")
    except Exception as e:
        print(f"An unexpected error occurred in lipsync_start: {e}. Skipping lipsync.")

@api_view(['GET'])
def get_data(request):
    global playAudio, change_flag
    data = {
        "message": "This is data from the Django backend! hehe",
        "playAudio": playAudio,
        'script': 'output',
        'changeFlag': change_flag
    }
    return Response(data)

@api_view(['POST'])
def start_non_verbal_interview(request):
    global stop_nv, non_verbal_data
    non_verbal_data = {
        "good_posture": 0,
        "unclear_posture": 0,
        "good_eye_contact": 0,
        "no_eye_contact": 0,
    }
    try:
        cap=set_non_verbal()
        mp_pose = mp.solutions.pose
        mp_drawing = mp.solutions.drawing_utils
        # Pose Estimation Loop
        start_time = time.time()
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret or stop_nv:
                    stop_nv=False
                    cap.release()
                    cv2.destroyAllWindows()
                    break

                # Convert to RGB for MediaPipe
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                result = pose.process(rgb_frame)

                # Draw pose landmarks
                if result.pose_landmarks:
                    mp_drawing.draw_landmarks(frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)

                    # Evaluate Posture
                    posture,eye_contact = evaluate_posture(result.pose_landmarks.landmark,mp_pose)

                    # Update frequency counts every 2 seconds
                    elapsed_time = time.time() - start_time
                    if elapsed_time >= 2:
                        start_time = time.time()  # Reset the timer
                        if posture == "Good Posture":
                            non_verbal_data["good_posture"] += 1
                        elif posture == "Unclear Posture":
                            non_verbal_data["unclear_posture"] += 1

                        if eye_contact == "Good eye contact":
                            non_verbal_data["good_eye_contact"] += 1
                        elif eye_contact == "No eye contact":
                            non_verbal_data["no_eye_contact"] += 1


                    # Display Feedback on Screen
                    cv2.putText(frame, posture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    cv2.putText(frame, eye_contact, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

                # Show Webcam Output
                #cv2.imshow('Body Language Analysis', frame)

                # Exit on 'q' Key
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

        # Release Resources
        cap.release()
        cv2.destroyAllWindows()
        return Response({"message": "non verbal interview completed"}, status=200)
    except Exception as e:
        print(e)
        return Response({"error in non verbal interview": str(e)}, status=500)

@api_view(['POST'])
def start_interview(request):
    global stop_nv, non_verbal_data, playAudio, change_flag
    stop_nv = False
    interviewer_types = ["Challenging_interviewer", "Data_Collector_interviewer", "Conversational_interviewer", "Investigative_interviewer", "Enthusiastic_interviewer", "Silent_interviewer", "Stress_interviewer", "Inexperienced_interviewer", "Hiring_Manager_interviewer", "HR_Representative_interviewer", "Team_Member_interviewer"]
    random.seed()
    interviewer_type = random.choice(interviewer_types)
    print(f"{interviewer_type =}")

    try:
        job = "Ai software engineer"
        q_num = 10
        resume_file = request.FILES.get('resume_file', None)
        resume_text = request.data.get('resume_text', None)
        resume_content_for_evaluation = "Candidate did not provide a resume." # Default for evaluation

        if resume_file:
            # Handle file upload
            file_name = default_storage.save(resume_file.name, ContentFile(resume_file.read()))
            resume_path = os.path.join(settings.MEDIA_ROOT, file_name)
            resume = get_resume(resume_path)
            print(f"from uploaded resume:{resume}")
        elif resume_text:
            # Use the provided resume text
            resume = "NO RESUME PROVIDED"
            print(f"from imported resume:{resume}")
        else:
            resume="'no resume data provided'"
            print(f"from default resume:{resume}")
        chat=get_chat(resume,job,interviewer_type,total_q_num=q_num)

        player = GTTSTTSPlayer(lang="en", slow=False)
        r = set_ear()
        print("Talk something to check microphone...")
        player.play_text("Please say something to check your microphone.")
        lipsync_start()
        trans_check = Listen(r)
        if trans_check:
            print(f"Mic check heard: {trans_check}")
            player.play_text("Great, your microphone is working. Let's start the interview.")
            time.sleep(0.5)
            lipsync_start()
        else:
            print("Mic check: No speech detected. Proceeding anyway.")
            player.play_text("I couldn't hear you clearly, but let's proceed with the interview.")
            lipsync_start()
        print("Microphone check completed.")
        
        # REMOVED: Sentence completeness model loading
        # results_path = os.path.join(settings.BASE_DIR,'myapp', 'str_comp_test', 'results')
        # print(f"{results_path =}")
        # tokenizer, model, device = set_sentance_complete(results_path=results_path) 
        # print("completeness check model loaded")

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        interview_folder = os.path.join(settings.BASE_DIR, 'myapp', 'interviews', f'interview_{timestamp}')
        os.makedirs(interview_folder, exist_ok=True)
        
        user_audio_folder = os.path.join(interview_folder, 'user_audio')
        os.makedirs(user_audio_folder, exist_ok=True)
        gemini_responses_file = os.path.join(interview_folder, 'gemini_responses.txt') # Still used for Gemini
        metadata_file = os.path.join(interview_folder, 'metadata.txt')
        non_verbal_data_file = os.path.join(interview_folder, 'non_verbal_data.txt')
        user_responses_file = os.path.join(interview_folder, 'user_responses.txt') # Renamed for clarity

        with open(metadata_file, 'w') as f:
            f.write(f"Interview Timestamp: {timestamp}\n")
            f.write(f"Job: {job}\n")
            f.write(f"Interviewer Type: {interviewer_type}\n") # This is the Gemini interviewer style
            f.write(f"Resume Provided: {'Yes' if resume_file or resume_text else 'No'}\n")

        player.play_text("So let's get into it without any delay.")
        lipsync_start()
        
        all_user_responses = []
        gemini_responses_log = [] # To log questions from Gemini

        # Initial prompt to Gemini to start the conversation / ask the first question
        # This might be handled inside get_chat or requires an initial message.
        # For simplicity, let's assume the first call to stream_complete_sentences with an empty/initial transcript gets the first question.
        current_response_for_gemini = "[[START INTERVIEW]]" # Initial prompt

        for i in range(q_num):
            question_number = i + 1
            print(f"--- Interaction {question_number} ---")
            
            # Get question/statement from Gemini
            gemini_question_text = ""
            print(f"Sending to Gemini for Q{question_number}: '{current_response_for_gemini[:50]}...'")
            for token in stream_complete_sentences(current_response_for_gemini, chat):
                gemini_question_text += token
                player.play_text(token)
                lipsync_start()
            
            if not gemini_question_text.strip():
                print(f"Gemini did not provide a response for interaction {question_number}. Ending interview early.")
                player.play_text("It seems we have a technical difficulty. Let's conclude the interview here.")
                lipsync_start()
                break # Exit the loop

            print(f"Gemini (Question/Statement {question_number}): {gemini_question_text}")
            gemini_responses_log.append(f"Gemini Utterance {question_number}: {gemini_question_text}")
            with open(gemini_responses_file, 'a') as f:
                 f.write(f"Gemini Utterance {question_number}: {gemini_question_text}\n")

            # Now, get user's response to this
            user_answer_response = ""
            successful_listen = False
            print("Please provide your answer now...")

            for attempt in range(3): # Allow up to 3 attempts to capture speech
                print(f"Listening attempt {attempt + 1} for user response to Gemini's utterance {question_number}...")
                try:
                    audio, trans = Listen(r)
                    if trans:
                        user_answer_response = trans
                        user_audio_filename = os.path.join(user_audio_folder, f'user_response_to_gemini_{question_number}_attempt{attempt+1}.wav')
                        with wave.open(user_audio_filename, 'wb') as wf:
                            wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(44100)
                            wf.writeframes(audio.get_wav_data())
                        successful_listen = True
                        print(f"Captured user response: {user_answer_response}")
                        break 
                    else:
                        print(f"No speech detected on attempt {attempt + 1}")
                except Exception as e:
                    print(f"Error during Listen() on attempt {attempt + 1}: {e}")
            
            if not successful_listen:
                print(f"No response captured from user for Gemini's utterance {question_number} after 3 attempts.")
                user_answer_response = "[[User did not respond]]"
            
            all_user_responses.append(user_answer_response)
            with open(user_responses_file, 'a') as f:
                f.write(f"User Response to Gemini Utterance {question_number}: {user_answer_response}\n")

            current_response_for_gemini = user_answer_response # Next input to Gemini is user's last answer

        stop_nv = True
        print("Interview loop completed.")
        player.play_text("Thank you, that concludes the interview.")
        lipsync_start()

        with open(non_verbal_data_file, 'w') as f:
            json.dump(non_verbal_data, f, indent=4)

        print("Starting evaluation phase...")
        
        metadata = {}
        try:
            with open(metadata_file, 'r') as f:
                for line in f:
                    if ": " in line:
                        key, value = line.strip().split(": ", 1)
                        metadata[key] = value
        except FileNotFoundError:
            print(f"Metadata file not found: {metadata_file}")
        
        user_audio_file_paths = []
        if os.path.exists(user_audio_folder):
            for filename in sorted(os.listdir(user_audio_folder)):
                if filename.endswith(".wav"):
                    user_audio_file_paths.append(os.path.join(user_audio_folder, filename))
        
        filler_words_count=count_filler_words(user_audio_file_paths)
        print(f"{filler_words_count =}")
        # Prepare the data to be sent to the frontend
        interview_data = {
            "gemini_responses": gemini_responses_log,
            "metadata": metadata,
            "non_verbal_results": non_verbal_data,
            "user_audio_files": user_audio_file_paths,
            "interview_folder":interview_folder,
            "user_responses": all_user_responses,
            "filler_words_count": filler_words_count,
        }
        print(f"{interview_data =}")
        try:
            score = evaluation_score(interview_data)
            print(f"{score =}")
        except Exception as e:
            print(f"Error in evaluation_score: {e}")
            return Response({"error": "Error in evaluation_score"}, status=500)
        ##########################################

        return Response({"message": "interview completed", "redirect_url": "/interview_results", "score": score}, status=200) #change the /results to your results page url
    except Exception as e:
        print(e)
        return Response({"error": str(e)}, status=500)