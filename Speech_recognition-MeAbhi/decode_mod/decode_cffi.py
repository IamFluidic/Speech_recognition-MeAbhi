# auto-generated file
import _cffi_backend

ffi = _cffi_backend.FFI('decode_mod.decode',
    _version = 0x2601,
    _types = b'\x00\x00\x04\x0D\x00\x00\x65\x03\x00\x00\x00\x0F\x00\x00\x1C\x0D\x00\x00\x60\x03\x00\x00\x0D\x01\x00\x00\x00\x0F\x00\x00\x0B\x0D\x00\x00\x01\x11\x00\x00\x00\x0F\x00\x00\x1F\x0D\x00\x00\x62\x03\x00\x00\x0D\x01\x00\x00\x00\x0F\x00\x00\x1F\x0D\x00\x00\x0B\x11\x00\x00\x0D\x01\x00\x00\x64\x03\x00\x00\x00\x0F\x00\x00\x1F\x0D\x00\x00\x0B\x11\x00\x00\x0D\x01\x00\x00\x01\x11\x00\x00\x00\x0F\x00\x00\x11\x0D\x00\x00\x01\x11\x00\x00\x00\x0F\x00\x00\x01\x0D\x00\x00\x61\x03\x00\x00\x00\x0F\x00\x00\x01\x0D\x00\x00\x63\x03\x00\x00\x00\x0F\x00\x00\x2B\x0D\x00\x00\x1C\x11\x00\x00\x00\x0F\x00\x00\x2B\x0D\x00\x00\x0B\x11\x00\x00\x01\x11\x00\x00\x00\x0F\x00\x00\x2B\x0D\x00\x00\x1F\x11\x00\x00\x01\x11\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x2B\x0D\x00\x00\x1F\x11\x00\x00\x05\x03\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x2B\x0D\x00\x00\x1F\x11\x00\x00\x66\x03\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x67\x0D\x00\x00\x04\x11\x00\x00\x00\x0F\x00\x00\x67\x0D\x00\x00\x1C\x11\x00\x00\x00\x0F\x00\x00\x67\x0D\x00\x00\x1C\x11\x00\x00\x01\x11\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x67\x0D\x00\x00\x1C\x11\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x67\x0D\x00\x00\x0B\x11\x00\x00\x00\x0F\x00\x00\x67\x0D\x00\x00\x1F\x11\x00\x00\x00\x0F\x00\x00\x67\x0D\x00\x00\x1F\x11\x00\x00\x11\x11\x00\x00\x00\x0F\x00\x00\x67\x0D\x00\x00\x1F\x11\x00\x00\x01\x11\x00\x00\x00\x0F\x00\x00\x67\x0D\x00\x00\x1F\x11\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x67\x0D\x00\x00\x11\x11\x00\x00\x00\x0F\x00\x00\x67\x0D\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x67\x0D\x00\x00\x00\x0F\x00\x00\x00\x09\x00\x00\x01\x09\x00\x00\x02\x09\x00\x00\x03\x09\x00\x00\x04\x09\x00\x00\x02\x01\x00\x00\x05\x01\x00\x00\x00\x01',
    _globals = (b'\x00\x00\x37\x23vosk_batch_model_free',0,b'\x00\x00\x00\x23vosk_batch_model_new',0,b'\x00\x00\x37\x23vosk_batch_model_wait',0,b'\x00\x00\x3D\x23vosk_batch_recognizer_accept_waveform',0,b'\x00\x00\x3A\x23vosk_batch_recognizer_finish_stream',0,b'\x00\x00\x3A\x23vosk_batch_recognizer_free',0,b'\x00\x00\x1B\x23vosk_batch_recognizer_front_result',0,b'\x00\x00\x21\x23vosk_batch_recognizer_get_pending_chunks',0,b'\x00\x00\x03\x23vosk_batch_recognizer_new',0,b'\x00\x00\x3A\x23vosk_batch_recognizer_pop',0,b'\x00\x00\x42\x23vosk_batch_recognizer_set_nlsml',0,b'\x00\x00\x5E\x23vosk_gpu_init',0,b'\x00\x00\x5E\x23vosk_gpu_thread_init',0,b'\x00\x00\x24\x23vosk_model_find_word',0,b'\x00\x00\x46\x23vosk_model_free',0,b'\x00\x00\x07\x23vosk_model_new',0,b'\x00\x00\x28\x23vosk_recognizer_accept_waveform',0,b'\x00\x00\x2D\x23vosk_recognizer_accept_waveform_f',0,b'\x00\x00\x32\x23vosk_recognizer_accept_waveform_s',0,b'\x00\x00\x1E\x23vosk_recognizer_final_result',0,b'\x00\x00\x49\x23vosk_recognizer_free',0,b'\x00\x00\x0A\x23vosk_recognizer_new',0,b'\x00\x00\x13\x23vosk_recognizer_new_grm',0,b'\x00\x00\x0E\x23vosk_recognizer_new_spk',0,b'\x00\x00\x1E\x23vosk_recognizer_partial_result',0,b'\x00\x00\x49\x23vosk_recognizer_reset',0,b'\x00\x00\x1E\x23vosk_recognizer_result',0,b'\x00\x00\x50\x23vosk_recognizer_set_grm',0,b'\x00\x00\x54\x23vosk_recognizer_set_max_alternatives',0,b'\x00\x00\x54\x23vosk_recognizer_set_nlsml',0,b'\x00\x00\x54\x23vosk_recognizer_set_partial_words',0,b'\x00\x00\x4C\x23vosk_recognizer_set_spk_model',0,b'\x00\x00\x54\x23vosk_recognizer_set_words',0,b'\x00\x00\x5B\x23vosk_set_log_level',0,b'\x00\x00\x58\x23vosk_spk_model_free',0,b'\x00\x00\x18\x23vosk_spk_model_new',0),
    _struct_unions = ((b'\x00\x00\x00\x60\x00\x00\x00\x10VoskBatchModel',),(b'\x00\x00\x00\x61\x00\x00\x00\x10VoskBatchRecognizer',),(b'\x00\x00\x00\x62\x00\x00\x00\x10VoskModel',),(b'\x00\x00\x00\x63\x00\x00\x00\x10VoskRecognizer',),(b'\x00\x00\x00\x64\x00\x00\x00\x10VoskSpkModel',)),
    _typenames = (b'\x00\x00\x00\x60VoskBatchModel',b'\x00\x00\x00\x61VoskBatchRecognizer',b'\x00\x00\x00\x62VoskModel',b'\x00\x00\x00\x63VoskRecognizer',b'\x00\x00\x00\x64VoskSpkModel'),
)
