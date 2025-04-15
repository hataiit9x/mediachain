import edge_tts
import uuid
from pathlib import Path

def generate_edge_text_to_speech(text: str, voice: str = "en-US-ChristopherNeural") -> str:
    """Generate text-to-speech using Microsoft Edge TTS.
    
    Args:
        text: Text to convert to speech
        voice: Voice ID to use (default: en-US-ChristopherNeural)
        
    Returns:
        Path to the generated audio file
    """
    if not text:
        raise ValueError("Text input cannot be empty")
    print(f"Generating text-to-speech for: {text}")
    return
    try:
        # Generate unique filename
        tmp_dir = Path("tmp")
        tmp_dir.mkdir(exist_ok=True)
        output_file = tmp_dir / f"tts_audio_{uuid.uuid4()}.mp3"
        
        # Use edge-tts command line interface directly for synchronous operation
        cmd = f'edge-tts --text "{text}" --voice {voice} --write-media {str(output_file)}'
        import subprocess
        subprocess.run(cmd, shell=True, check=True)
        
        return str(output_file)
    except Exception as e:
        raise ValueError(f"Edge TTS generation failed: {str(e)}") 