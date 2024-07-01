import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]


plt.figure(figsize=(8, 5))

plt.plot(x, y, marker='o', linestyle='-', color='b', label='Veri')  # Çizgi grafiği oluştur

plt.title('Basit Bir Çizim')
plt.xlabel('X ekseni')
plt.ylabel('Y ekseni')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()