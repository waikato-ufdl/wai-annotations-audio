# wai-annotations-audio
wai.annotations module for audio processing.

The manual is available here:

https://ufdl.cms.waikato.ac.nz/wai-annotations-manual/

## Plugins
### CONVERT-TO-MONO-AC
Converts audio files to mono (audio classification).

#### Domain(s):
- **Audio classification domain**

#### Options:
```
usage: convert-to-mono-ac [-s SAMPLE_RATE]

optional arguments:
  -s SAMPLE_RATE, --sample-rate SAMPLE_RATE
                        the sample rate to use for the audio data. (default: 22050)
```

### CONVERT-TO-MONO-SP
Converts audio files to mono (speech domain)

#### Domain(s):
- **Speech Domain**

#### Options:
```
usage: convert-to-mono-sp [-s SAMPLE_RATE]

optional arguments:
  -s SAMPLE_RATE, --sample-rate SAMPLE_RATE
                        the sample rate to use for the audio data. (default: 22050)
```


### CONVERT-TO-WAV-AC
Converts mp3/flac/ogg to wav for audio classification domain.

#### Domain(s):
- **Audio classification domain**

#### Options:
```
usage: convert-to-wav-ac [-s SAMPLE_RATE]

optional arguments:
  -s SAMPLE_RATE, --sample-rate SAMPLE_RATE
                        the sample rate to use for the WAV data. (default: 22050)
```


### CONVERT-TO-WAV-SP
Converts mp3/flac/ogg to wav for speech domain.

#### Domain(s):
- **Speech Domain**

#### Options:
```
usage: convert-to-wav-sp [-s SAMPLE_RATE]

optional arguments:
  -s SAMPLE_RATE, --sample-rate SAMPLE_RATE
                        the sample rate to use for the WAV data. (default: 22050)
```

