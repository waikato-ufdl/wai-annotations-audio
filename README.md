# wai-annotations-audio
wai.annotations module for audio processing.

The manual is available here:

https://ufdl.cms.waikato.ac.nz/wai-annotations-manual/

## Plugins
### CONVERT-TO-MONO
Converts audio files to monophonic.

#### Domain(s):
- **Speech Domain**
- **Audio classification domain**

#### Options:
```
usage: convert-to-mono
```


### CONVERT-TO-WAV
Converts mp3/flac/ogg to wav.

#### Domain(s):
- **Speech Domain**
- **Audio classification domain**

#### Options:
```
usage: convert-to-wav [-s SAMPLE_RATE]

optional arguments:
  -s SAMPLE_RATE, --sample-rate SAMPLE_RATE
                        the sample rate to use for the audio data, for overriding the native rate.
                        (default: None)
```


### RESAMPLE-AUDIO
Resamples audio files.

#### Domain(s):
- **Speech Domain**
- **Audio classification domain**

#### Options:
```
usage: resample-audio [-s SAMPLE_RATE] [-v]

optional arguments:
  -s SAMPLE_RATE, --sample-rate SAMPLE_RATE
                        the sample rate to use for the audio data. (default: 22050)
  -v, --verbose         whether to output some debugging output (default: False)
```


### STFT-SPECTROGRAM
Generates a plot from a short time fourier transform (STFT) spectrogram.

#### Domain(s):
- **Audio classification domain**

#### Options:
```
usage: stft-spectrogram [--center] [--dpi DPI] [--hop-length HOP_LENGTH] [--num-fft NUM_FFT]
                        [--pad-mode PAD_MODE] [--win-length WIN_LENGTH] [--window WINDOW]

optional arguments:
  --center              for centering the signal. (default: False)
  --dpi DPI             the dots per inch (default: 100)
  --hop-length HOP_LENGTH
                        number of audio samples between adjacent STFT columns. defaults to
                        win_length // 4 (default: None)
  --num-fft NUM_FFT     the length of the windowed signal after padding with zeros. should be power
                        of two. (default: 2048)
  --pad-mode PAD_MODE   used when 'centering' (default: constant)
  --win-length WIN_LENGTH
                        each frame of audio is windowed by window of length win_length and then
                        padded with zeros to match num_fft. defaults to win_length = num_fft
                        (default: None)
  --window WINDOW       a window function, such as scipy.signal.windows.hann (default: hann)
```


### TRIM-AUDIO
Trims silence from audio files.

#### Domain(s):
- **Audio classification domain**
- **Speech Domain**

#### Options:
```
usage: trim-audio [--frame-length FRAME_LENGTH] [--hop-length HOP_LENGTH] [--top-db TOP_DB] [-v]

optional arguments:
  --frame-length FRAME_LENGTH
                        the number of samples per analysis frame. (default: 2048)
  --hop-length HOP_LENGTH
                        the number of samples between analysis frames (default: 512)
  --top-db TOP_DB       the threshold (in decibels) below reference to consider as silence.
                        (default: 60)
  -v, --verbose         whether to output some debugging output (default: False)
```
