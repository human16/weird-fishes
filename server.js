const express = require('express');
const fs = require('fs');
const csv = require('csv-parser');
const app = express();
const PORT = 3000;

app.use(express.static('public'));

app.get('./rumfssf_matched_detections_2024_cleaned.csv', (req, res) => {
  const results = [];
  fs.createReadStream('rumfssf_matched_detections_2024_cleaned.csv')
    .pipe(csv())
    .on('data', (row) => {
      results.push(row);
    })
    .on('end', () => {
      res.json(results);
    });
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
