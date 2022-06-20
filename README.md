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
- **Audio classification domain**
- **Speech Domain**

#### Options:
```
usage: resample-audio [-s SAMPLE_RATE]

optional arguments:
  -s SAMPLE_RATE, --sample-rate SAMPLE_RATE
                        the sample rate to use for the audio data. (default: 22050)
```
