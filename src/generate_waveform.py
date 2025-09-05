"""
generate_waveform.py
====================

Generate synthetic SDR waveforms based on archetype frequency mapping.
Waveforms can be sine, square, triangle, or other simple forms, representing
emotional/cognitive states and Hemi-Sync resonance.

"""

import numpy as np
import yaml
import argparse
import os
from scipy.io.wavfile import write

# Default sample rate
SAMPLE_RATE = 48000

# Duration of each waveform in seconds
DURATION = 10

# Waveform generator functions
def sine_wave(freq, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate*duration), endpoint=False)
    return 0.5 * np.sin(2 * np.pi * freq * t)

def square_wave(freq, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate*duration), endpoint=False)
    return 0.5 * np.sign(np.sin(2 * np.pi * freq * t))

def triangle_wave(freq, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate*duration), endpoint=False)
    return 0.5 * 2 * np.abs(2*((freq*t) % 1) - 1) - 0.5

WAVEFORM_MAP = {
    "sine": sine_wave,
    "square": square_wave,
    "triangle": triangle_wave
}

def load_config(config_path):
    """Load SDR config YAML from given path."""
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def generate_archetype_waveform(archetype_info, output_dir="data/waveforms"):
    """Generate a waveform for a single archetype."""
    freq_mhz = archetype_info.get("frequency_mhz")
    waveform_type = archetype_info.get("waveform", "sine")
    archetype_name = archetype_info.get("archetype", "Unknown")
    
    if freq_mhz is None:
        print(f"Skipping {archetype_name}: no frequency defined.")
        return
    
    # Convert MHz to Hz
    freq_hz = freq_mhz * 1e6
    
    waveform_func = WAVEFORM_MAP.get(waveform_type, sine_wave)
    waveform = waveform_func(freq_hz, DURATION, SAMPLE_RATE)
    
    # Convert to 16-bit PCM
    waveform_int16 = np.int16(waveform * 32767)
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, f"{archetype_name.lower().replace(' ', '_')}_waveform.wav")
    write(output_path, SAMPLE_RATE, waveform_int16)
    
    print(f"Generated {output_path} ({waveform_type}, {freq_mhz} MHz)")

def main():
    parser = argparse.ArgumentParser(description="Generate SDR waveforms based on archetype mapping.")
    parser.add_argument(
        "--config",
        type=str,
        default="src/sdr_config.yaml",
        help="Path to SDR config YAML file (default: src/sdr_config.yaml)"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="data/waveforms",
        help="Output directory for generated waveforms"
    )
    
    args = parser.parse_args()
    
    config = load_config(args.config)
    
    for freq, info in config.get("frequencies", {}).items():
        info["frequency_mhz"] = float(freq)  # Ensure numeric
        generate_archetype_waveform(info, output_dir=args.output)

if __name__ == "__main__":
    main()
