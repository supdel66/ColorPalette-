from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import io

app = Flask(__name__)

def generate_palette(image, num_colors=5):
    image = image.resize((150, 150))
    rgb = image.convert("RGB")
    img_array = np.array(rgb)
    img_array = img_array.reshape((-1, 3))
    kmeans = KMeans(n_clusters=num_colors, random_state=42, n_init=10)
    kmeans.fit(img_array)
    colors = kmeans.cluster_centers_.astype(int)
    return colors

@app.route('/', methods=['GET'])
def hi():
    return "Hello, go to /palette!"


@app.route('/palette', methods=['POST'])
def palette_endpoint():
    file = request.files['image']
    num_colors = int(request.form.get('num_colors', 5))
    image = Image.open(io.BytesIO(file.read()))
    colors = generate_palette(image, num_colors)
    hex_colors = [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in colors]
    return jsonify({
        "palette": hex_colors,
        "rgb": colors.tolist()
    })

if __name__ == '__main__':
    app.run(debug=True)