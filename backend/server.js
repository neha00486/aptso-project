const express = require('express');
const cors = require('cors');
const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());

app.post('/search', (req, res) => {
  const { title, location } = req.body;
  console.log('Job Search Query:', title, location);

  // For now, just send a dummy response
  res.json({
    message: `Searching jobs for '${title}' in '${location}'...`,
  });
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
