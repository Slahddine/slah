# 📚 Calculateur de Notes (Student Grade Calculator)

A simple, client-side web application to manage subject grades and automatically calculate a weighted average with a final mention.

## Features

- Add subjects with a **name**, **grade** (0–20), and **coefficient**
- Instant **weighted average** calculation
- Automatic **mention** (Très Bien, Bien, Assez Bien, etc.)
- Pass / Fail result based on the 10/20 threshold
- Per-subject **appreciation** label (Excellent, Très Bien, …, Insuffisant)
- Delete individual subjects or clear the entire list
- Fully client-side — no installation, no server required

## How to Use

1. Open `index.html` in any modern web browser.
2. Enter a subject name, its grade (out of 20), and a coefficient.
3. Click **Ajouter** (or press **Enter**) to add it to the list.
4. The average, mention, and result update automatically.
5. Click the **✕** button on any row to remove that subject.
6. Click **🗑 Tout effacer** to start over.

## Grading Scale

| Average       | Mention                   |
|---------------|---------------------------|
| ≥ 16          | 🏆 Félicitations du jury  |
| 14 – 15.99    | 🥇 Très Bien              |
| 12 – 13.99    | 🥈 Bien                   |
| 10 – 11.99    | 🥉 Assez Bien             |
| < 10          | ❌ Ajourné(e)             |

## Project Structure

```
├── index.html   # Main HTML page
├── style.css    # Styles (responsive)
└── app.js       # Grade logic (pure JavaScript, no dependencies)
```

## Technologies

- HTML5
- CSS3 (CSS Grid / Flexbox)
- Vanilla JavaScript (ES6+)
