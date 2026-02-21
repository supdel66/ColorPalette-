# Palette API

A Flask API to generate color palettes from uploaded images.

## Endpoints

- `POST /palette`: Upload an image and get palette colors.

## Deploying to Railway

1. Push this repo to GitHub.
2. Create a new Railway project and link your GitHub repo.
3. Railway will auto-detect the Python app and use the `Procfile`.

## Running locally

```
pip install -r requirements.txt
python app.py
```

## Example Request

Use Postman or curl:

```
curl -X POST -F "image=@your_image.jpg" -F "num_colors=5" http://localhost:5000/palette
```
