import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_matrix_base(ax):
    # Рисуем контур матрицы
    rect = patches.Rectangle((0, 0), 10, 10, linewidth=2, edgecolor='black', facecolor='none')
    ax.add_patch(rect)
    # Рисуем диагональ
    ax.plot([0, 10], [10, 0], 'k--')
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 11)
    ax.axis('off')

def plot_pivot_col():
    fig, ax = plt.subplots(figsize=(3, 3))
    draw_matrix_base(ax)
    
    k = 4
    # Линии поиска
    ax.plot([k, k], [10-k, 0], 'k-', lw=1.5)
    ax.plot([0, 10], [10-k, 10-k], 'k:', alpha=0.5)
    
    # Точки
    ax.plot(k, 10-k, 'wo', markeredgecolor='black', markersize=8) # a_{kk}
    ax.plot(k, 3, 'ko', markersize=8) # a_{pk}
    
    # Подписи
    ax.text(-0.5, 10-k, 'k', va='center', ha='right', fontsize=12)
    ax.text(k, 10.5, 'k', ha='center', va='bottom', fontsize=12)
    ax.text(-0.5, 3, 'p', va='center', ha='right', fontsize=12)
    
    # Стрелки перестановки
    ax.annotate('', xy=(10.5, 10-k), xytext=(10.5, 3), 
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    
    plt.savefig('pivot_col.png', dpi=300, bbox_inches='tight', transparent=True)
    plt.close()

def plot_pivot_row():
    fig, ax = plt.subplots(figsize=(3, 3))
    draw_matrix_base(ax)
    
    k = 4
    # Линии поиска
    ax.plot([k, 10], [10-k, 10-k], 'k-', lw=1.5)
    ax.plot([k, k], [0, 10], 'k:', alpha=0.5)
    
    # Точки
    ax.plot(k, 10-k, 'wo', markeredgecolor='black', markersize=8)
    ax.plot(7.5, 10-k, 'ko', markersize=8) # a_{kq}
    
    # Подписи
    ax.text(-0.5, 10-k, 'k', va='center', ha='right', fontsize=12)
    ax.text(k, 10.5, 'k', ha='center', va='bottom', fontsize=12)
    ax.text(7.5, 10.5, 'q', ha='center', va='bottom', fontsize=12)
    
    # Стрелки перестановки
    ax.annotate('', xy=(k, -0.5), xytext=(7.5, -0.5), 
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    
    plt.savefig('pivot_row.png', dpi=300, bbox_inches='tight', transparent=True)
    plt.close()

def plot_pivot_full():
    fig, ax = plt.subplots(figsize=(3, 3))
    draw_matrix_base(ax)
    
    k = 4
    # Прямоугольник поиска
    rect = patches.Rectangle((k, 0), 10-k, 10-k, linewidth=1.5, edgecolor='black', facecolor='none')
    ax.add_patch(rect)
    ax.plot([0, 10], [10-k, 10-k], 'k:', alpha=0.5)
    ax.plot([k, k], [0, 10], 'k:', alpha=0.5)
    
    # Точки
    ax.plot(k, 10-k, 'wo', markeredgecolor='black', markersize=8)
    ax.plot(7.5, 3, 'ko', markersize=8) # a_{pq}
    
    # Подписи
    ax.text(-0.5, 10-k, 'k', va='center', ha='right', fontsize=12)
    ax.text(k, 10.5, 'k', ha='center', va='bottom', fontsize=12)
    ax.text(-0.5, 3, 'p', va='center', ha='right', fontsize=12)
    ax.text(7.5, 10.5, 'q', ha='center', va='bottom', fontsize=12)
    
    # Стрелки перестановки
    ax.annotate('', xy=(10.5, 10-k), xytext=(10.5, 3), 
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax.annotate('', xy=(k, -0.5), xytext=(7.5, -0.5), 
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    
    plt.savefig('pivot_full.png', dpi=300, bbox_inches='tight', transparent=True)
    plt.close()

if __name__ == '__main__':
    plot_pivot_col()
    plot_pivot_row()
    plot_pivot_full()
    print("Графики выбора главного элемента успешно сгенерированы!")
