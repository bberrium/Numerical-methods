# Лекция 4: LU-разложение и Метод Гаусса

## LU-метод



Пусть имеем $Ax = b, \ \det A \neq 0$.

**Теорема (LU-разложение):**


Пусть все угловые миноры матрицы $A \in \mathbb{R}^{n \times n}$ отличны от нуля, т.е.

$$A \binom{1 \ 2 \ ... \ k}{1 \ 2 \ ... \ k} \neq 0 \quad k = \overline{1, n}$$

Тогда матрицу $A$ можно представить, причём единственным образом, в виде произведения:


$$A = LU$$


где $L$ — нижняя треугольная матрица с ненулевыми диагональными элементами, а $U$ — верхняя треугольная матрица с единицами на главной диагонали.

$$L = \begin{bmatrix} l_{11} & & & 0 \\ l_{21} & \ddots & & \\ & & \ddots & \\ & & & l_{nn} \end{bmatrix} \quad \forall l_{ii} \neq 0; \quad U = \begin{bmatrix} 1 & & & \\ 0 & 1 & & \\ & & \ddots & \\ & & & 1 \end{bmatrix}$$

**Теорема:** Произведение нижних (верхних) треугольных матриц есть нижняя (верхняя) треугольная матрица.
**Теорема:** Матрица, обратная к нижней (верхней) треугольной матрице, есть нижняя (верхняя) треугольная матрица.

Предположим, удалось найти LU-разложение матрицы $A$. Тогда:

$$Ax = b \Rightarrow LUx = b$$

$$\begin{cases} Ly = b \\ Ux = y \end{cases} \quad \left. \begin{array}{l} \\ \end{array} \right\} \approx 2n^2 \text{ операций}$$

Основная трудность — в нахождении разложения.

---

### Алгоритм Краута



$A = [a_{ij}]_{n \times n}, \quad L = [l_{ij}]_{n \times n} \ (l_{ij} = 0, \text{ если } i < j)$


$U = [u_{ij}]_{n \times n} \ (u_{ij} = 0, \text{ если } i > j, \ u_{ii} = 1)$

$$A = LU = \begin{bmatrix} l_{11} & & 0 \\ l_{21} & l_{22} & \\ \dots & \dots & \dots \\ l_{n1} & l_{n2} & \dots & l_{nn} \end{bmatrix} \begin{bmatrix} 1 & u_{12} & \dots & u_{1n} \\ & 1 & \dots & u_{2n} \\ 0 & & \ddots & \dots \\ & & & 1 \end{bmatrix}$$

$$a_{ij} = \sum_{k=1}^n l_{ik} u_{kj} = l_{i1} u_{1j} \quad j = \overline{1, n}$$

$$a_{i1} = l_{i1}; \quad \text{если } j \ge 2 \quad u_{1j} = \frac{a_{1j}}{l_{11}} \quad j = \overline{2, n}$$

В общем виде:


$$a_{ij} = \sum_{k=1}^n l_{ik} u_{kj} = \sum_{k=1}^{\min(i, j)} l_{ik} u_{kj} \quad i = \overline{2, n}, \ j = \overline{2, n}$$

Зафиксируем некоторую строку $i, \ 1 \le i \le n$.

* Если $j \le i$: $a_{ij} = \sum_{k=1}^j l_{ik} u_{kj}$

* Если $j > i$: $a_{ij} = \sum_{k=1}^i l_{ik} u_{kj}$


Отделим последние члены сумм (помним, что $u_{jj} = 1$):

* Если $j \le i$: $a_{ij} = \sum_{k=1}^{j-1} l_{ik} u_{kj} + l_{ij} \underbrace{u_{jj}}_{=1}$

* Если $j > i$: $a_{ij} = \sum_{k=1}^{i-1} l_{ik} u_{kj} + l_{ii} u_{ij}$


Тогда получаем расчетные формулы:

* $j = \overline{1, i}: \quad l_{ij} = a_{ij} - \sum_{k=1}^{j-1} l_{ik} u_{kj}$

* $j = \overline{i+1, n}: \quad u_{ij} = \frac{a_{ij} - \sum_{k=1}^{i-1} l_{ik} u_{kj}}{l_{ii}}$


> 💡 **Объяснение:** Алгоритм Краута позволяет шаг за шагом "вытаскивать" элементы матриц L и U из исходной матрицы A, не решая огромных систем. Суть в том, что формулы строго упорядочены: чтобы посчитать следующий неизвестный элемент $l_{ij}$ или $u_{ij}$, мы используем только те элементы матриц $L$ и $U$, которые уже вычислили на предыдущих шагах.

**Псевдокод алгоритма Краута:**

```c++
input n, A = [a_ij]
l_11 = a_11
for j = 2 .. n
    u_1j = a_1j / l_11
end
for i = 2 .. n
    for j = 1 .. i
        l_ij = a_ij - sum_{k=1}^{j-1} (l_ik * u_kj)   # (1) -> 2 \sum_{j=1}^i (j-1) операций
    end
    u_ii = 1
    for j = i+1 .. n
        u_ij = (a_ij - sum_{k=1}^{i-1} (l_ik * u_kj)) / l_ii # (2) -> \sum_{j=i+1}^n (2i-1) операций
    end
end
output (l_ij), (u_ij)
```
**Подсчет количества операций ($A_{ops}$) для LU-разложения:**
$$A_{ops} = (n-1) + \sum_{i=2}^n \left[ 2\sum_{j=1}^i (j-1) + \sum_{j=i+1}^n (2i-1) \right] =$$
$$= (n-1) + \sum_{i=2}^n \left[ 2 \frac{1 + (i-1)}{2} (i-1) + (2i-1)(n - (i+1) + 1) \right] =$$

$$= (n-1) + \sum_{i=2}^n [ i(i-1) + (2i-1)(n-i) ] = (n-1) + \sum_{i=2}^n (-i^2 + 2ni - n) =$$
$$= -\sum_{i=1}^n i^2 + 2n\sum_{i=1}^n i - n(n-1) + n - 1 =$$
$$= -\sum_{i=1}^n i^2 + 2n\sum_{i=1}^n i - n^2 + 2n - 1 = -\frac{n(n+1)(2n+1)}{6} + 2n \frac{2+n}{2}(n-1) - n^2 + 2n =$$
$$= -\frac{n^3}{3} + n^3 + ... \approx \frac{2}{3} n^3$$
**Вывод:** $A_{ops} \approx \frac{2}{3} n^3$.

---

## Метод Гаусса

$$\begin{cases} a_{11}x_1 + a_{12}x_2 + ... + a_{1n}x_n = b_1 \\ a_{21}x_1 + a_{22}x_2 + ... + a_{2n}x_n = b_2 \quad (1) \\ \dots \\ a_{n1}x_1 + a_{n2}x_2 + ... + a_{nn}x_n = b_n \end{cases}$$


**Алгоритм:**
Предположим, $a_{11} \neq 0$. Разделим первое уравнение на $a_{11}$:
$$x_1 + u_{12}x_2 + ... + u_{1n}x_n = y_1 \quad (2)$$

где $u_{1j} = \frac{a_{1j}}{a_{11}} \quad j = \overline{2, n}, \quad y_1 = \frac{b_1}{a_{11}}$

Далее последовательно умножая (2) на $a_{i1}, \ i = \overline{2, n}$ и вычитая полученное уравнение из $i$-го уравнения системы (1), приходим к системе уравнений:

$$\begin{cases} x_1 + u_{12}x_2 + ... + u_{1n}x_n = y_1 \\ \qquad a_{22}^{(1)}x_2 + ... + a_{2n}^{(1)}x_n = b_2^{(1)} \\ \qquad \dots \\ \qquad a_{n2}^{(1)}x_2 + ... + a_{nn}^{(1)}x_n = b_n^{(1)} \end{cases}$$

где
$$a_{ij}^{(1)} = a_{ij} - a_{i1}u_{1j} \quad i=\overline{2,n}, \ j=\overline{2,n}$$

$$b_i^{(1)} = b_i - a_{i1}y_1 \quad i=\overline{2,n}$$


Проделав аналогично $n$ шагов, придём к системе уравнений с верхней треугольной матрицей:
$$\begin{cases} x_1 + u_{12}x_2 + ... + u_{1,n-1}x_{n-1} + u_{1n}x_n = y_1 \\ \qquad x_2 + ... + u_{2,n-1}x_{n-1} + u_{2n}x_n = y_2 \\ \qquad \dots \dots \dots \dots \\ \qquad \qquad \qquad x_{n-1} + u_{n-1,n}x_n = y_{n-1} \\ \qquad \qquad \qquad \qquad \qquad \quad x_n = y_n \end{cases}$$


**Получим (общие формулы прямого хода):**
$a_{ij}^{(0)} = a_{ij} \quad i=\overline{1,n}, \ j=\overline{1,n}; \quad b_i^{(0)} = b_i \quad i=\overline{1,n}$

Для шагов $k = 1, \dots, n-1$:
$$u_{kj} = \frac{a_{kj}^{(k-1)}}{a_{kk}^{(k-1)}} \quad j = \overline{k+1, n}; \quad y_k = \frac{b_k^{(k-1)}}{a_{kk}^{(k-1)}}$$

$$a_{ij}^{(k)} = a_{ij}^{(k-1)} - a_{ik}^{(k-1)} \cdot u_{kj} \quad i=\overline{k+1, n}, \ j=\overline{k+1, n}$$

$$b_i^{(k)} = b_i^{(k-1)} - a_{ik}^{(k-1)} y_k \quad i=\overline{k+1, n}$$


Для $k = n$:
$$y_n = \frac{b_n^{(n-1)}}{a_{nn}^{(n-1)}}$$


**Второй этап — обратная подстановка:**
$$x_n = y_n$$

$$x_i = y_i - \sum_{j=i+1}^n u_{ij}x_j \quad i = n-1, n-2, ..., 1$$

