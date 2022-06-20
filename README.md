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


### PITCH-SHIFT
Augmentation method for shifting the pitch of audio files.

#### Domain(s):
- **Speech Domain**
- **Audio classification domain**

#### Options:
```
usage: pitch-shift [-m AUG_MODE] [--suffix AUG_SUFFIX] [--bins-per-octave BINS_PER_OCTAVE] [-s SEED]
                   [-a] [-f STEPS_FROM] [-t STEPS_TO] [-T THRESHOLD]

optional arguments:
  -m AUG_MODE, --mode AUG_MODE
                        the audio augmentation mode to use, available modes: replace, add (default:
                        replace)
  --suffix AUG_SUFFIX   the suffix to use for the file names in case of augmentation mode add
                        (default: None)
  --bins-per-octave BINS_PER_OCTAVE
                        how many steps per octave (default: 12.0)
  -s SEED, --seed SEED  the seed value to use for the random number generator; randomly seeded if
                        not provided (default: None)
  -a, --seed-augmentation
                        whether to seed the augmentation; if specified, uses the seeded random
                        generator to produce a seed value from 0 to 1000 for the augmentation.
                        (default: False)
  -f STEPS_FROM, --from-steps STEPS_FROM
                        the minimum (fractional) steps to shift (default: None)
  -t STEPS_TO, --to-steps STEPS_TO
                        the maximum (fractional) steps to shift (default: None)
  -T THRESHOLD, --threshold THRESHOLD
                        the threshold to use for Random.rand(): if equal or above, augmentation gets
                        applied; range: 0-1; default: 0 (= always) (default: None)
```


### RESAMPLE-AUDIO
Resamples audio files.

For resample types, see:
https://librosa.org/doc/latest/generated/librosa.resample.html#librosa.resample

#### Domain(s):
- **Audio classification domain**
- **Speech Domain**

#### Options:
```
usage: resample-audio [-t RESAMPLE_TYPE] [-s SAMPLE_RATE] [-v]

optional arguments:
  -t RESAMPLE_TYPE, --resample-type RESAMPLE_TYPE
                        the resampling type to apply (kaiser_best|kaiser_fast|fft|polyphase|linear|z
                        ero_order_hold|sinc_best|sinc_medium|sinc_fastest|soxr_vhq|soxr_hq|soxr_mq|s
                        oxr_lq|soxr_qq) (default: kaiser_best)
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
