import os
import re
from moviepy import VideoFileClip

# Caminho da pasta onde estão os vídeos .mp4
pasta_videos = "/caminho/para/sua/pasta"

# Quantidade de minutos que você quer estudar por dia (ex: 60 minutos = 1 hora)
minutos_por_dia = 60

# Função para extrair o número do início do nome do arquivo (ex: "1.-Introducao.mp4" -> 1)
def chave_numerica(nome_arquivo):
    m = re.match(r"^(\d+)", nome_arquivo)  # Regex pega números no início da string
    return int(m.group(1)) if m else float('inf')  # Se não achar número, manda pro final da lista

# Função que calcula a duração de um vídeo em segundos
def get_duracao_em_segundos(caminho_video):
    try:
        clip = VideoFileClip(caminho_video)  # Abre o vídeo
        duracao = clip.duration  # Pega a duração em segundos
        clip.close()  # Fecha o vídeo para liberar memória
        return duracao
    except Exception as e:
        print(f"Erro ao ler {caminho_video}: {e}")
        return 0  # Se der erro, considera duração 0 para evitar travar o script

# Função que formata segundos para o formato "Xh Ymin Zs"
def formatar_tempo(segundos):
    horas = int(segundos // 3600)
    minutos = int((segundos % 3600) // 60)
    segundos_restantes = int(segundos % 60)
    return f"{horas}h {minutos}min {segundos_restantes}s"

def main():
    # Lista todos os arquivos .mp4 na pasta
    videos = [f for f in os.listdir(pasta_videos) if f.lower().endswith(".mp4")]

    # Ordena os vídeos de forma numérica (ex: 1, 2, 3, ..., 10, 11, ...)
    videos.sort(key=chave_numerica)

    total_segundos = 0  # Vai acumular o tempo total de todos os vídeos
    lista_duracoes = []  # Guarda (nome_do_arquivo, duração_em_segundos) de cada vídeo

    # Calcula a duração de cada vídeo
    for video in videos:
        caminho_completo = os.path.join(pasta_videos, video)
        duracao = get_duracao_em_segundos(caminho_completo)
        total_segundos += duracao
        lista_duracoes.append((video, duracao))

    # Formata o tempo total do curso
    tempo_total_formatado = formatar_tempo(total_segundos)

    dias = []  # Lista de listas → cada dia terá uma lista de vídeos
    dia_atual = []  # Vídeos do dia atual
    acumulado_dia = 0  # Tempo acumulado no dia atual

    # Divide os vídeos por dia (meta: minutos_por_dia minutos por dia)
    for video, duracao in lista_duracoes:
        acumulado_dia += duracao
        dia_atual.append(video)

        # Se atingir ou ultrapassar o tempo diário, salva o dia e começa outro
        if acumulado_dia >= minutos_por_dia * 60:
            dias.append(dia_atual)
            dia_atual = []
            acumulado_dia = 0

    # Se ainda sobrar vídeos no último dia (menos de 1h), salva também
    if dia_atual:
        dias.append(dia_atual)

    # Prepara o conteúdo de saída
    saida = []
    saida.append(f"Tempo total do curso: {tempo_total_formatado}")
    saida.append(f"Quantidade total de dias (estudando {minutos_por_dia} minutos por dia): {len(dias)}\n")

    # Adiciona o planejamento por dia
    for idx, dia in enumerate(dias, 1):
        saida.append(f"Dia {idx}:")
        for video in dia:
            saida.append(f"  - {video}")
        saida.append("")  # Linha em branco entre os dias

    # Salva o resultado em um arquivo .txt na mesma pasta dos vídeos
    arquivo_saida = os.path.join(pasta_videos, "planejamento_estudo.txt")
    with open(arquivo_saida, "w", encoding="utf-8") as f:
        f.write("\n".join(saida))

    print(f"\nPlanejamento gerado com sucesso!")
    print(f"Arquivo salvo em: {arquivo_saida}")

if __name__ == "__main__":
    main()
