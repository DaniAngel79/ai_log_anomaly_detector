import pandas as pd
import torch
import argparse
import sys
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# --- CONFIGURACIÓN DE MODELO ---
# Usamos el modelo especializado en logs que ya tenías identificado
MODEL_PATH = "d4rk-lucif3r/autotrain-log_anomaly_detection-881525996"

def detect_anomalies(log_lines):
    """Clasificación de logs mediante Deep Learning (Transformers)."""
    try:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
        model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
        
        results = []
        for line in log_lines:
            line = line.strip()
            if not line: continue
            
            inputs = tokenizer(line, return_tensors="pt", truncation=True, padding=True)
            with torch.no_grad():
                outputs = model(**inputs)
            
            prediction = torch.argmax(outputs.logits, dim=1).item()
            status = "ANOMALÍA" if prediction == 1 else "Normal"
            results.append((line, status))
        return results
    except Exception as e:
        print(f"[!] Error cargando modelo IA: {e}. Usando Fallback de firmas.")
        return detect_anomalies_fallback(log_lines)

def detect_anomalies_fallback(log_lines):
    """Detección basada en firmas (Keywords) para resiliencia del sistema."""
    keywords = ["ERROR", "FATAL", "PANIC", "TIMEOUT", "FAIL"]
    results = []
    for line in log_lines:
        line = line.strip()
        if not line: continue
        is_anomaly = any(k in line.upper() for k in keywords)
        status = "ANOMALÍA (Firma)" if is_anomaly else "Normal"
        results.append((line, status))
    return results

def main():
    parser = argparse.ArgumentParser(description="AI Log Anomaly Detector PoC")
    parser.add_argument("--file", help="Ruta al archivo .log a analizar")
    args = parser.parse_args()

    print("--- MONITOR DE ANOMALÍAS INICIADO ---")
    
    if args.file:
        log_path = Path(args.file)
        if not log_path.exists():
            print(f"Error: El archivo {args.file} no existe.")
            sys.exit(1)
        lines = log_path.read_text().splitlines()
    else:
        # Ejemplo por defecto si no se pasa archivo
        print("[*] No se detectó archivo. Usando set de muestras dinámico...")
        lines = [
            "ERROR: System reboot failed, kernel panic detected.",
            "INFO: User danilo logged in successfully.",
            "WARNING: Low disk space on /var/log, 10% remaining."
        ]

    anomalies = detect_anomalies(lines)

    print(f"\n{'ESTADO':<20} | {'CONTENIDO DEL LOG'}")
    print("-" * 60)
    for log, status in anomalies:
        print(f"{status:<20} | {log}")

if __name__ == "__main__":
    main()
