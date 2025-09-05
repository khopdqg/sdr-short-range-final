"""
analyze_waveform.py
===================

Analyze synthetic SDR waveforms and produce FFT plots.
Labels are drawn from archetype mapping and resonance states.

"""

import numpy as np
import matplotlib.pyplot as plt
import argparse
from scipy.io import wavfile
import os
import yaml

def load_config(config_path="src/sdr_config.yaml"):
    """Load SDR archetype configuration from YAML."""
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def analyze_waveform(file_path, config, output_dir="data/plots"):
    """Analyze a single waveform and save its FFT plot."""
    # Read waveform
    sample_rate, data = wavfile.read(file_path)
    data = data.astype(float) / 32767  # Convert from 16-bit PCM

    n = len(data)
    fft_data = np.fft.fft(data)
    fft_freq = np.fft.fftfreq(n, d=1/sample_rate)
    
    # Only positive frequencies
    pos_mask = fft_freq >= 0
    fft_data = np.abs(fft_data[pos_mask])
    fft_freq = fft_freq[pos_mask] / 1e6  # Convert Hz to MHz

    # Attempt to match archetype by frequency
    archetype_label = "Unknown"
    for freq, info in config.get("frequencies", {}).items():
        target_freq = float(freq)
        if np.any(np.isclose(fft_freq, target_freq, atol=0.5)):
            archetype_label = info.get("archetype", "Unknown")
            break

    # Plot FFT
    plt.figure(figsize=(10, 6))
    plt.plot(fft_freq, fft_data, color='blue')
    plt.title(f"FFT of {os.path.basename(file_path)} – Archetype: {archetype_label}")
    plt.xlabel("Frequency (MHz)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, os.path.basename(file_path).replace(".wav", "_fft.png"))
    plt.savefig(output_path)
    plt.close()
    
    print(f"FFT plot saved: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Analyze SDR waveform and plot FFT")
    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Path to waveform .wav file"
    )
    parser.add_argument(
        "--config",
        type=str,
        default="src/sdr_config.yaml",
        help="Path to SDR config YAML (default: src/sdr_config.yaml)"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="data/",
        help="Directory to save FFT plots"
    )
    args = parser.parse_args()

    config = load_config(args.config)
    analyze_waveform(args.input, config, output_dir=args.output)

if __name__ == "__main__":
    main()
