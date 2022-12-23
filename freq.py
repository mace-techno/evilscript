import numpy as np

# Set the frequency range and step size
start_frequency = 100  # Hz
end_frequency = 1000  # Hz
step_size = 50  # Hz

# Generate a list of frequencies to scan
frequencies = np.arange(start_frequency, end_frequency, step_size)

# Set the noise level
noise_level = 0.1  # relative units

# Scan the frequencies
for frequency in frequencies:
    # Generate a synthetic signal at the current frequency
    signal = np.sin(2*np.pi*frequency*t)

    # Add some noise to the signal
    noise = np.random.normal(0, noise_level, len(signal))
    signal += noise

    # Process the signal to extract the frequency and intensity
    extracted_frequency = # code to extract frequency goes here
    intensity = # code to extract intensity goes here

    # Print the results
    print(f"Frequency: {extracted_frequency} Hz, Intensity: {intensity}")




    import numpy as np
from scipy import signal

# Set the frequency range and step size
start_frequency = 100  # Hz
end_frequency = 1000  # Hz
step_size = 50  # Hz

# Generate a list of frequencies to scan
frequencies = np.arange(start_frequency, end_frequency, step_size)

# Set the noise level
noise_level = 0.1  # relative units

# Set the sampling rate
sampling_rate = 10000  # Hz

# Set the length of the signal in seconds
signal_length = 0.1  # seconds

# Generate a time vector for the signal
t = np.arange(0, signal_length, 1/sampling_rate)

# Scan the frequencies
for frequency in frequencies:
    # Generate a synthetic signal at the current frequency
    signal = np.sin(2*np.pi*frequency*t)

    # Add some noise to the signal
    noise = np.random.normal(0, noise_level, len(signal))
    signal += noise

    # Apply a low-pass filter to remove high-frequency noise
    fc = 500  # Hz
    b, a = signal.butter(4, fc/(sampling_rate/2), 'lowpass')
    filtered_signal = signal.filtfilt(b, a, signal)

    # Perform a Fourier transform to extract the frequency components of the signal
    fft_output = np.fft.fft(filtered_signal)
    fft_frequencies = np.fft.fftfreq(len(signal), 1/sampling_rate)

    # Find the peak frequency in the FFT output
    peak_frequency_index = np.argmax(np.abs(fft_output))
    extracted_frequency = fft_frequencies[peak_frequency_index]

    # Extract the intensity of the signal
    intensity = np.abs(fft_output[peak_frequency_index])

    # Print the results
    print(f"Frequency: {extracted_frequency} Hz, Intensity: {intensity}")

    


