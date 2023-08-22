from flask import Flask, render_template, request
import cv2
import os

app = Flask(__name__)

def create_data(video_path):
    output_dir = 'frames1/'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    cap = cv2.VideoCapture(video_path)
    
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
    
        frame_filename = os.path.join(output_dir, f'frame_{frame_count:04d}.jpg')
        cv2.imwrite(frame_filename, frame)
    
        frame_count += 1

    cap.release()
    cv2.destroyAllWindows()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_path = request.form['video_path']
        create_data(video_path)
        return 'Video frames created successfully!'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
