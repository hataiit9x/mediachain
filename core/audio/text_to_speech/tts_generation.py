from core.audio.text_to_speech.services.openai import generate_openai_text_to_speech
from core.audio.text_to_speech.services.azure_openai import generate_azure_openai_text_to_speech
from core.audio.text_to_speech.services.elevenlabs import generate_elevenlabs_text_to_speech
from core.audio.text_to_speech.services.edge import generate_edge_text_to_speech
from typing import Literal

# Available voices for each service
EDGE_VOICES = [
    "en-US-ChristopherNeural",  # Male
    "en-US-JennyNeural",        # Female
    "en-US-AriaNeural",         # Female
    "en-US-GuyNeural",          # Male
    "en-GB-SoniaNeural",        # British Female
    "en-GB-RyanNeural",         # British Male
]

# todo: Literal for voice in each service. E.g. elevenlabs voice ["Brian", "Adam", "Rachel"], openai voice ["alloy", "echo", "fable", "nova", "shimmer"]

def generate_text_to_speech(
    service: Literal["openai", "azure_openai", "elevenlabs", "edge"], 
    api_key: str, 
    text: str, 
    voice: str, 
    azure_config: dict = None
) -> str:
    """Generate text-to-speech using the specified service.
    
    Args:
        service: TTS service to use ("openai", "azure_openai", "elevenlabs", or "edge")
        api_key: API key for the service (not needed for edge)
        text: Text to convert to speech
        voice: Voice ID to use
        azure_config: Configuration for Azure OpenAI (only needed for azure_openai)
        
    Returns:
        Path to the generated audio file
    """
    if service == "openai":
        try:
            return generate_openai_text_to_speech(api_key, text, voice)
        except Exception as e:
            raise ValueError(f"Error generating text-to-speech with OpenAI: {e}")
    elif service == "azure_openai":
        try:
            return generate_azure_openai_text_to_speech(api_key, text, voice, azure_config)
        except Exception as e:
            raise ValueError(f"Error generating text-to-speech with Azure OpenAI: {e}")
    elif service == "elevenlabs":
        try:
            return generate_elevenlabs_text_to_speech(api_key, text, voice)
        except Exception as e:
            raise ValueError(f"Error generating text-to-speech with ElevenLabs: {e}")
    elif service == "edge":
        try:
            return generate_edge_text_to_speech(text, voice)
        except Exception as e:
            raise ValueError(f"Error generating text-to-speech with Edge TTS: {e}")
    else:
        raise ValueError(f"Invalid text-to-speech service: {service}")