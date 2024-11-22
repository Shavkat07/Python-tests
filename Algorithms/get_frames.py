import cv2
import os

def video_to_frames(video_path, output_folder):
    """Разделить видео на кадры и сохранить их."""
    # Убедиться, что выходная папка существует
    os.makedirs(output_folder, exist_ok=True)

    # Открыть видеофайл
    video_capture = cv2.VideoCapture(video_path)

    # Проверить, удалось ли открыть видео
    if not video_capture.isOpened():
        print(f"Error: Cannot open video {video_path}")
        return

    frame_count = 0
    while True:
        # Читаем очередной кадр
        ret, frame = video_capture.read()

        # Если кадр не удалось прочитать (конец видео), выходим из цикла
        if not ret:
            break

        # Сохраняем кадр как изображение
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.png")
        cv2.imwrite(frame_filename, frame)

        frame_count += 1

    # Освобождаем ресурсы
    video_capture.release()
    print(f"Video split into {frame_count} frames and saved to {output_folder}")

# Пример использования
video_path = "../media/stickman_running.webm"  # Укажите путь к вашему видеофайлу
output_folder = "frames"         # Папка для сохранения кадров
video_to_frames(video_path, output_folder)


