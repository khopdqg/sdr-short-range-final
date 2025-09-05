# SDR Short-Range Prototype

## Overview
This repository contains tools and documentation for the generation, capture, and analysis of short-range software-defined radio (SDR) signals. The project focuses on experimental testing of signal modulation and waveform analysis in a controlled environment.

## Contents
- `src/`: Source code for waveform generation, signal simulation, and analysis.
- `data/`: Example waveforms, captured signals, and plots.
- `docs/`: Technical documentation, configuration notes, and experiment logs.

## Functionality
The scripts in this repository enable users to:
1. Generate synthetic SDR waveforms according to predefined parameters.
2. Analyze waveform characteristics using frequency-domain techniques.
3. Produce plots and reports summarizing signal properties.

## Configuration
Signal parameters, archetype mappings, and waveform specifications are defined in `src/sdr_config.yaml`. Users can adjust these values to explore different signal characteristics.

## Usage
### Generating a waveform
```bash
python src/generate_waveform.py --frequency 144.5
```
### Analyzing a waveform
```bash
python src/analyze_waveform.py --input data/waveforms/hero_waveform.wav
```
## Notes
All data and waveforms generated in this repository are synthetic and intended for experimental or educational purposes. No signals are intended for transmission over licensed radio frequencies.
