import tensorflow as tf
import tensorflow_io as tfio


def convert_audio_to_spectrogram(filepath, nfft, window_size_samples, stride_size_samples):
    audio = tfio.audio.AudioIOTensor(filepath)
    print(audio)
    audio_slice = audio[:]
    audio_tensor = tf.squeeze(audio_slice, axis=[-1])
    if audio_tensor.dtype != tf.float32:
        audio_tensor = tf.cast(audio_tensor, tf.float32) / 32768.0
    position = tfio.audio.trim(audio_tensor, axis=0, epsilon=0.1)
    start = position[0]
    stop = position[1]
    processed = audio_tensor[start:stop]
    spectrogram = tfio.audio.spectrogram(
        processed, nfft=nfft, window=window_size_samples, stride=stride_size_samples)
    return spectrogram
