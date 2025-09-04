import os
from moviepy import VideoFileClip

# Caminho da pasta com os vídeos
pasta_videos = "/caminho/para/sua/pasta"

# Quantos minutos de estudo por dia
minutos_por_dia = 60

def get_duracao_em_segundos(caminho_video):
    try:
        clip = VideoFileClip(caminho_video)
        duracao = clip.duration  # duração em segundos
        clip.close()
        return duracao
    except Exception as e:
        print(f"Erro ao ler {caminho_video}: {e}")
        return 0

def formatar_tempo(segundos):
    horas = int(segundos // 3600)
    minutos = int((segundos % 3600) // 60)
    segundos_restantes = int(segundos % 60)
    return f"{horas}h {minutos}min {segundos_restantes}s"

def main():
    # Listar todos os arquivos .mp4
    videos = [f for f in os.listdir(pasta_videos) if f.lower().endswith(".mp4")]
    videos.sort()  # Ordenar por nome

    total_segundos = 0
    lista_duracoes = []

    # Calcular a duração de cada vídeo
    for video in videos:
        caminho_completo = os.path.join(pasta_videos, video)
        duracao = get_duracao_em_segundos(caminho_completo)
        total_segundos += duracao
        lista_duracoes.append((video, duracao))

    # Calcular total em horas:minutos:segundos
    tempo_total_formatado = formatar_tempo(total_segundos)

    # Dividir em dias
    dias = []
    dia_atual = []
    acumulado_dia = 0

    for video, duracao in lista_duracoes:
        acumulado_dia += duracao
        dia_atual.append(video)

        if acumulado_dia >= minutos_por_dia * 60:
            dias.append(dia_atual)
            dia_atual = []
            acumulado_dia = 0

    # Se sobrar vídeos no último dia
    if dia_atual:
        dias.append(dia_atual)

    # Criar o texto de saída
    saida = []
    saida.append(f"Tempo total do curso: {tempo_total_formatado}")
    saida.append(f"Quantidade total de dias (estudando {minutos_por_dia} minutos por dia): {len(dias)}\n")

    for idx, dia in enumerate(dias, 1):
        saida.append(f"Dia {idx}:")
        for video in dia:
            saida.append(f"  - {video}")
        saida.append("")  # Linha em branco entre os dias

    # Exportar para um arquivo .txt
    arquivo_saida = os.path.join(pasta_videos, "planejamento_estudo.txt")
    with open(arquivo_saida, "w", encoding="utf-8") as f:
        f.write("\n".join(saida))

    print(f"\nPlanejamento gerado com sucesso!")
    print(f"Arquivo salvo em: {arquivo_saida}")

if __name__ == "__main__":
    main()
