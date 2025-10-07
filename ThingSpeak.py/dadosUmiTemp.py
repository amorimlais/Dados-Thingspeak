import random
import datetime
import matplotlib.pyplot as plt

# --- 1. Gerar dados fictícios de temperatura e umidade ---
num_dados = 20  # quantidade de medições simuladas

# Gerando tempos simulados (um intervalo de 5 minutos entre cada dado)
tempo = [datetime.datetime.now() - datetime.timedelta(minutes=5 * i) for i in range(num_dados)]
tempo.reverse()  # deixar em ordem cronológica

# Gerar dados aleatórios simulando sensores
temperatura = [round(random.uniform(22.0, 35.0), 1) for _ in range(num_dados)]  # °C
umidade = [round(random.uniform(40.0, 90.0), 1) for _ in range(num_dados)]      # %

# --- 2. Exibir dados simulados ---
print("Leituras simuladas de sensores (temperatura e umidade):\n")
for t, temp, umi in zip(tempo, temperatura, umidade):
    print(f"{t.strftime('%H:%M:%S')} -> Temperatura: {temp}°C | Umidade: {umi}%")

# --- 3. Criar o Dashboard (gráficos) ---
plt.figure(figsize=(10, 5))

# Gráfico da Temperatura
plt.subplot(1, 2, 1)
plt.plot(tempo, temperatura, color='red', marker='o', linestyle='-')
plt.title("Temperatura (°C)")
plt.xlabel("Tempo")
plt.ylabel("Temperatura")
plt.xticks(rotation=45)
plt.grid(True)

# Gráfico da Umidade
plt.subplot(1, 2, 2)
plt.plot(tempo, umidade, color='blue', marker='o', linestyle='-')
plt.title("Umidade (%)")
plt.xlabel("Tempo")
plt.ylabel("Umidade")
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()
