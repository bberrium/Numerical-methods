# Лекция 3: Нормы и Спектральный радиус

## Норма Фробениуса и Операторная норма

**Норма Фробениуса:**


$$\vert{}\vert{}A\vert{}\vert{}_F = \left( \sum_{i,j=1}^n \vert{}a_{ij}\vert{}^2 \right)^{\frac{1}{2}}$$

**Операторная норма:**


$$\vert{}\vert{}A\vert{}\vert{} = \max_{x \neq 0} \frac{\vert{}\vert{}Ax\vert{}\vert{}}{\vert{}\vert{}x\vert{}\vert{}} \quad (*)$$

**Свойства операторной нормы:**

1. $\vert{}\vert{}I\vert{}\vert{} = 1$

2. $\vert{}\vert{}Ax\vert{}\vert{} \le \vert{}\vert{}A\vert{}\vert{} \cdot \vert{}\vert{}x\vert{}\vert{}$


*Замечание:* $\vert{}\vert{}I\vert{}\vert{}_F = \sqrt{n}$ (поэтому норма Фробениуса не является операторной, т.к. нарушается свойство 1).

### Вычисление операторной нормы

$$\vert{}\vert{}A\vert{}\vert{}_\infty = \max_{x \neq 0} \frac{\vert{}\vert{}Ax\vert{}\vert{}_\infty}{\vert{}\vert{}x\vert{}\vert{}_\infty}$$

Из $(*)$ следует:


$$\frac{\vert{}\vert{}Ax\vert{}\vert{}}{\vert{}\vert{}x\vert{}\vert{}} = \left\vert{}\left\vert{} \frac{1}{\vert{}\vert{}x\vert{}\vert{}} Ax \right\vert{}\right\vert{} = \left\vert{}\left\vert{} A \left( \frac{1}{\vert{}\vert{}x\vert{}\vert{}} x \right) \right\vert{}\right\vert{} = \vert{}\vert{}Ay\vert{}\vert{}$$


где $y = \frac{1}{\vert{}\vert{}x\vert{}\vert{}}x$, следовательно $\vert{}\vert{}y\vert{}\vert{} = 1$.

Тогда:


$$\vert{}\vert{}A\vert{}\vert{}_\infty = \max_{\vert{}\vert{}x\vert{}\vert{}_\infty = 1} \vert{}\vert{}Ax\vert{}\vert{}_\infty \quad (*)$$

Пусть $A = [a_{ij}]_{n \times n}$.
Возьмём $\forall x = \begin{bmatrix} x_1 \\ ... \\ x_n \end{bmatrix}$ ; $\vert{}\vert{}x\vert{}\vert{}_\infty = 1$.

Рассмотрим:


$$\vert{}\vert{}Ax\vert{}\vert{}_\infty = \max_{1 \le i \le n} \vert{}(Ax)_i\vert{} \quad \text{($i$-ая компонента)}$$

$$= \max_{1 \le i \le n} \left\vert{} \sum_{j=1}^n a_{ij} x_j \right\vert{} \le \max_{1 \le i \le n} \sum_{j=1}^n \vert{}a_{ij}\vert{} \cdot \vert{}x_j\vert{} \le \max_{1 \le i \le n} \sum_{j=1}^n \vert{}a_{ij}\vert{}$$

Следовательно:


$$\vert{}\vert{}A\vert{}\vert{}_\infty \le \max_{1 \le i \le n} \sum_{j=1}^n \vert{}a_{ij}\vert{}$$

*Хотим показать, что равно. Получим обратное неравенство:*

$$\exists \ 1 \le i_0 \le n ; \quad \max_{1 \le i \le n} \sum_{j=1}^n \vert{}a_{ij}\vert{} = \sum_{j=1}^n \vert{}a_{i_0 j}\vert{}$$


(максимум достигается на какой-то строке $i_0$).

Составим вектор $z = \begin{bmatrix} z_1 \\ ... \\ z_n \end{bmatrix}$, где:


$$z_j = \begin{cases} \frac{\vert{}a_{i_0 j}\vert{}}{a_{i_0 j}}, & a_{i_0 j} \neq 0 \\ 1, & a_{i_0 j} = 0 \end{cases}$$

Очевидно, $\vert{}\vert{}z\vert{}\vert{}_\infty = 1 \Rightarrow \vert{}\vert{}A\vert{}\vert{}_\infty \ge \vert{}\vert{}Az\vert{}\vert{}_\infty$ (в силу $(*)$).

$$\Rightarrow \max_{1 \le i \le n} \vert{}(Az)_i\vert{} = \max_{1 \le i \le n} \left\vert{} \sum_{j=1}^n a_{ij} z_j \right\vert{} \ge \left\vert{} \sum_{j=1}^n a_{i_0 j} z_j \right\vert{} = \sum_{j=1}^n \vert{}a_{i_0 j} z_j\vert{} = \sum_{j=1}^n \vert{}a_{i_0 j}\vert{} = \max_{1 \le i \le n} \sum_{j=1}^n \vert{}a_{ij}\vert{}$$

Отсюда:


$$\vert{}\vert{}A\vert{}\vert{}_\infty = \max_{1 \le i \le n} \sum_{j=1}^n \vert{}a_{ij}\vert{}$$

---

Для $l_1$-нормы:


$$\vert{}\vert{}x\vert{}\vert{}_1 = \sum_{i=1}^n \vert{}x_i\vert{}$$

$$\vert{}\vert{}A\vert{}\vert{}_1 = \max_{\vert{}\vert{}x\vert{}\vert{}_1 = 1} \vert{}\vert{}Ax\vert{}\vert{}_1$$

**Вывод формулы для $\vert{}\vert{}A\vert{}\vert{}_1$:**


$$(\le)$$


Возьм. $\forall x = \begin{bmatrix} x_1 \\ ... \\ x_n \end{bmatrix}, \ \vert{}\vert{}x\vert{}\vert{}_1 = 1$.

$$\vert{}\vert{}Ax\vert{}\vert{}_1 = \sum_{i=1}^n \vert{}(Ax)_i\vert{} = \sum_{i=1}^n \left\vert{} \sum_{j=1}^n a_{ij} x_j \right\vert{} \le \sum_{i=1}^n \sum_{j=1}^n \vert{}a_{ij}\vert{} \cdot \vert{}x_j\vert{} = \sum_{j=1}^n \sum_{i=1}^n \vert{}a_{ij}\vert{} \cdot \vert{}x_j\vert{} \le \max_{1 \le j \le n} \sum_{i=1}^n \vert{}a_{ij}\vert{} \cdot \underbrace{\sum_{j=1}^n \vert{}x_j\vert{}}_{=1} \Rightarrow$$

$$\Rightarrow \vert{}\vert{}Ax\vert{}\vert{}_1 \le \max_{1 \le j \le n} \sum_{i=1}^n \vert{}a_{ij}\vert{} \quad \text{(при } \max_{\vert{}\vert{}x\vert{}\vert{}_1=1})$$

$$\Rightarrow \vert{}\vert{}A\vert{}\vert{}_1 \le \max_{1 \le j \le n} \sum_{i=1}^n \vert{}a_{ij}\vert{}$$

$$(\ge)$$


Пусть $\max_{1 \le j \le n} \sum_{i=1}^n \vert{}a_{ij}\vert{} = \sum_{i=1}^n \vert{}a_{i j_0}\vert{} \quad \exists \ 1 \le j_0 \le n$.
Возьмем вектор $z = \begin{bmatrix} z_1 \\ ... \\ z_n \end{bmatrix}$, где:


$$z_i = \begin{cases} 1, & i = j_0 \\ 0, & i \neq j_0 \end{cases}; \quad \vert{}\vert{}z\vert{}\vert{}_1 = 1$$

$$\vert{}\vert{}A\vert{}\vert{}_1 \ge \vert{}\vert{}Az\vert{}\vert{}_1 = \sum_{i=1}^n \vert{}(Az)_i\vert{} = \sum_{i=1}^n \left\vert{} \sum_{j=1}^n a_{ij} z_j \right\vert{} = \sum_{i=1}^n \vert{}a_{i j_0}\vert{} = \max_{1 \le j \le n} \sum_{i=1}^n \vert{}a_{ij}\vert{}$$

Отсюда:


$$\vert{}\vert{}A\vert{}\vert{}_1 = \max_{1 \le j \le n} \sum_{i=1}^n \vert{}a_{ij}\vert{}$$

**Пример:**
$A = \begin{bmatrix} 1 & -2 & 3 \\ -4 & 1 & 1 \\ 5 & 6 & -9 \end{bmatrix} \begin{matrix} 6 \\ 6 \\ 20 \end{matrix}$ (сумма модулей по строкам)
$10 \quad 9 \quad 13$ (сумма модулей по столбцам)
$\Rightarrow \vert{}\vert{}A\vert{}\vert{}_\infty = 20$
$\vert{}\vert{}A\vert{}\vert{}_1 = 13$

---

### Спектральная норма ($l_2$)

$$\vert{}\vert{}x\vert{}\vert{}_2 = \left( \sum_{i=1}^n \vert{}x_i\vert{}^2 \right)^{\frac{1}{2}}$$

$$\vert{}\vert{}x\vert{}\vert{}_2 = \sqrt{(x, x)}$$

Найдём $\vert{}\vert{}A\vert{}\vert{}_2$:
Возьмём $\forall x; \ \vert{}\vert{}x\vert{}\vert{}_2 = 1$.
Рассм. $\vert{}\vert{}Ax\vert{}\vert{}_2 = \max_{x \neq 0} \frac{\vert{}\vert{}Ax\vert{}\vert{}_2}{\vert{}\vert{}x\vert{}\vert{}_2} = \max_{x \neq 0} \frac{\sqrt{(Ax, Ax)}}{\sqrt{(x, x)}}$ (чтоб не писать корни, возведем в квадрат)

$$= \max_{x \neq 0} \frac{(Ax, Ax)}{(x, x)} = \max_{x \neq 0} \frac{(A^T Ax, x)}{(x, x)}$$

$(Ax, y) = (x, A^T y) \Rightarrow \lambda_{\max} (A^T A)$


$A^T A$ — симметричная и положительно полуопределённая.
$(A^T Ax, x) = (Ax, Ax) \ge 0$.

Следовательно:


$$\vert{}\vert{}A\vert{}\vert{}_2 = \sqrt{\lambda_{\max}(A^T A)}$$

**Пример:** $A = \begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix}$


$A^T = \begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix}$


$A^T A = \begin{bmatrix} 1 & 2 \\ 2 & 5 \end{bmatrix} \to$ симм.
$\begin{vmatrix} 1-\lambda & 2 \\ 2 & 5-\lambda \end{vmatrix} = 0 \Rightarrow (1-\lambda)(5-\lambda) - 4 = 0 \Rightarrow \lambda^2 - 6\lambda + 1 = 0 \Rightarrow \lambda = 3 \pm \sqrt{8} = 3 \pm 2\sqrt{2}$.
$\sqrt{3 + 2\sqrt{2}}$ — норма этой матрицы.

**Частные случаи:**

1. $A = A^T$, симм.
$\lambda_{\max}(A^T A) = \lambda_{\max}(A^2) = (\max \vert{}\lambda(A)\vert{})^2 \Rightarrow \vert{}\vert{}A\vert{}\vert{}_2 = \max \vert{}\lambda(A)\vert{}$.


2. $A = A^T \ge 0$, полож. полуопр.
$\vert{}\vert{}A\vert{}\vert{}_2 = \max \lambda(A)$.



---

### Эквивалентность норм

Пусть имеем линейное пр-о $L$, введены 2 нормы: $\vert{}\vert{} \cdot \vert{}\vert{}_{(1)}$ и $\vert{}\vert{} \cdot \vert{}\vert{}_{(2)}$.
Говорят, что нормы **эквивалентны**, если $\exists \ c_1, c_2 > 0$ (const):

$$c_1 \vert{}\vert{}x\vert{}\vert{}_{(2)} \le \vert{}\vert{}x\vert{}\vert{}_{(1)} \le c_2 \vert{}\vert{}x\vert{}\vert{}_{(2)}$$


(1 норма оценивается через другую).

Напр. имеем послед. $x_k \xrightarrow[k \to \infty]{} x$, это означает $\vert{}\vert{}x_k - x\vert{}\vert{} \xrightarrow[k \to \infty]{} 0$.
Если посл. сходится в одной норме, то сходится и в другой.
$c_1 \vert{}\vert{}x_k - x\vert{}\vert{}_{(2)} \le \vert{}\vert{}x_k - x\vert{}\vert{}_{(1)} \le c_2 \vert{}\vert{}x_k - x\vert{}\vert{}_{(2)}$.

---

## Матричные ряды и Ряд Неймана

Степенной матричный ряд:


$$\sum_{k=0}^\infty A^k \to \text{Ряд Неймана (Джон фон)}$$

Как понимаем сходимость?
Сост. $S_m(A) = \sum_{k=0}^m A^k$ — $S_1(A), S_2(A), ...$
Ряд сходится, если сход. посл. его частичных сумм.

$$\sum_{k=0}^\infty A^k = \lim_{m \to \infty} S_m(A)$$

**Утв.** $\sum_{k=0}^\infty A^k = \lim_{m \to \infty} S_m(A) \iff \rho(A) < 1$. (Необх. и дост. усл.)

Пусть ряд сход., тогда чему равна сумма ряда?

$$(I - A)S_m(A) = (I - A)(I + A + A^2 + ... + A^m) = I - A^{m+1}$$

$$S_m(A) = (I - A)^{-1}(I - A^{m+1})$$

$$\lim_{m \to \infty} S_m(A) = (I - A)^{-1} (I - \lim_{m \to \infty} A^{m+1}) = (I - A)^{-1}$$


$\Rightarrow$ 

$$\sum_{k=0}^\infty A^k = (I - A)^{-1}$$

Утв., что $\det(I - A) \neq 0$:
Собств. числа — это корни $\det(\lambda I - A) = 0$.
Если бы $\det = 0, \Rightarrow \lambda = 1$, но $\rho(A) < 1 \Rightarrow \det(I - A) \neq 0$ и $\exists (I - A)^{-1}$.

> 💡 **Объяснение:** Ряд Неймана — это матричный аналог бесконечной геометрической прогрессии. В школе мы учили, что сумма $1 + q + q^2 + \dots = \frac{1}{1-q}$, если $\vert{}q\vert{} < 1$. В мире матриц роль $\vert{}q\vert{}$ играет спектральный радиус $\rho(A)$ (модуль самого большого собственного значения). Если он меньше 1, то бесконечная сумма матриц $I + A + A^2 + \dots$ сходится к матрице $(I-A)^{-1}$.

Число $\sum_{k=0}^\infty a^k$: если $\vert{}a\vert{} < 1$, то $\frac{1}{1-a} = (1-a)^{-1}$.

Собств. числа сложно оценить, не всегда можно посчитать.

$$\rho(A) \le \vert{}\vert{}A\vert{}\vert{}$$

**Док:** Рассм. $A, \ \lambda$ собств. знач, $x$ собств. вектор: $Ax = \lambda x$.
Составим матрицу $B = [x \ \ 0 \ \ 0 \ \ \dots \ \ 0] \neq 0$.

$$AB = [Ax \ \ 0 \ \ \dots \ \ 0] = [\lambda x \ \ 0 \ \ \dots \ \ 0] = \lambda B$$

$$\vert{}\vert{}\lambda B\vert{}\vert{} = \vert{}\vert{}AB\vert{}\vert{} \le \vert{}\vert{}A\vert{}\vert{} \cdot \vert{}\vert{}B\vert{}\vert{}$$

$$\vert{}\lambda\vert{} \cdot \vert{}\vert{}B\vert{}\vert{} \le \vert{}\vert{}A\vert{}\vert{} \cdot \vert{}\vert{}B\vert{}\vert{} \Rightarrow \vert{}\lambda\vert{} \le \vert{}\vert{}A\vert{}\vert{}$$


## Число обусловленности матрицы

Пусть имеем систему линейных алгебраических уравнений с невырожденной матрицей:


$$Ax = b \quad (\det A \neq 0)$$

Предположим, вектор правой части $b$ задан с погрешностью $\Delta b$, что вызывает погрешность решения $\Delta x$:


$$A(x + \Delta x) = b + \Delta b$$

Какова относительная погрешность $\frac{\vert{}\vert{}\Delta x\vert{}\vert{}}{\vert{}\vert{}x\vert{}\vert{}}$ через $\frac{\vert{}\vert{}\Delta b\vert{}\vert{}}{\vert{}\vert{}b\vert{}\vert{}}$?
Раскроем скобки:


$$Ax + A\Delta x = b + \Delta b$$


Так как $Ax = b$, получаем:


$$A\Delta x = \Delta b \Rightarrow \Delta x = A^{-1} \Delta b$$

Возьмём норму от обеих частей (существует операторная норма):


$$\vert{}\vert{}\Delta x\vert{}\vert{} = \vert{}\vert{}A^{-1} \Delta b\vert{}\vert{} \le \vert{}\vert{}A^{-1}\vert{}\vert{} \cdot \vert{}\vert{}\Delta b\vert{}\vert{} = \vert{}\vert{}A^{-1}\vert{}\vert{} \cdot \vert{}\vert{}b\vert{}\vert{} \cdot \frac{\vert{}\vert{}\Delta b\vert{}\vert{}}{\vert{}\vert{}b\vert{}\vert{}}$$

С другой стороны, из $Ax = b$ следует:


$$\vert{}\vert{}b\vert{}\vert{} = \vert{}\vert{}Ax\vert{}\vert{} \le \vert{}\vert{}A\vert{}\vert{} \cdot \vert{}\vert{}x\vert{}\vert{}$$

Подставим это ограничение для $\vert{}\vert{}b\vert{}\vert{}$ в предыдущее неравенство:


$$\vert{}\vert{}\Delta x\vert{}\vert{} \le \vert{}\vert{}A^{-1}\vert{}\vert{} \cdot \vert{}\vert{}A\vert{}\vert{} \cdot \vert{}\vert{}x\vert{}\vert{} \cdot \frac{\vert{}\vert{}\Delta b\vert{}\vert{}}{\vert{}\vert{}b\vert{}\vert{}}$$


Поделив обе части на $\vert{}\vert{}x\vert{}\vert{}$, получаем:


$$\frac{\vert{}\vert{}\Delta x\vert{}\vert{}}{\vert{}\vert{}x\vert{}\vert{}} \le \vert{}\vert{}A\vert{}\vert{} \cdot \vert{}\vert{}A^{-1}\vert{}\vert{} \frac{\vert{}\vert{}\Delta b\vert{}\vert{}}{\vert{}\vert{}b\vert{}\vert{}}$$

Обозначим:


$$K(A) \equiv \vert{}\vert{}A\vert{}\vert{} \cdot \vert{}\vert{}A^{-1}\vert{}\vert{}$$


Это **число обусловленности матрицы**.

Следовательно, оценка относительной погрешности принимает вид:


$$\frac{\vert{}\vert{}\Delta x\vert{}\vert{}}{\vert{}\vert{}x\vert{}\vert{}} \le K(A) \frac{\vert{}\vert{}\Delta b\vert{}\vert{}}{\vert{}\vert{}b\vert{}\vert{}}$$

> 💡 **Объяснение:** Число обусловленности $K(A)$ показывает, во сколько раз может увеличиться относительная ошибка ответа по сравнению с относительной ошибкой исходных данных. Если $K(A)$ близко к 1, система "хорошая" (хорошо обусловлена). Если $K(A)$ огромное (например, $10^6$), то даже микроскопическая ошибка в исходных данных может полностью разрушить результат вычислений, сделав его неверным.

### Свойства числа обусловленности (индуцированные от нормы)



**1) $K(A) \ge 1$**


*Доказательство:*
Известно, что спектральный радиус $\rho(A) \le \vert{}\vert{}A\vert{}\vert{}$, то есть $\max \vert{}\lambda(A)\vert{} \le \vert{}\vert{}A\vert{}\vert{}$.
Для обратной матрицы: $\max \vert{}\lambda(A^{-1})\vert{} = \frac{1}{\min \vert{}\lambda(A)\vert{}} \le \vert{}\vert{}A^{-1}\vert{}\vert{}$.
Перемножим эти неравенства:


$$1 \le \frac{\max \vert{}\lambda(A)\vert{}}{\min \vert{}\lambda(A)\vert{}} \le \vert{}\vert{}A\vert{}\vert{} \cdot \vert{}\vert{}A^{-1}\vert{}\vert{} = K(A)$$

**2) $K(A^{-1}) = K(A)$**

**3) $K(AB) \le K(A) \cdot K(B)$**

Пусть у нас симметричная матрица $A = A^T$.
Рассмотрим число обусловленности во второй норме (спектральное число обусловленности):


$$K_2(A) = \vert{}\vert{}A\vert{}\vert{}_2 \cdot \vert{}\vert{}A^{-1}\vert{}\vert{}_2$$


Так как $\vert{}\vert{}A\vert{}\vert{}_2 = \max \vert{}\lambda(A)\vert{}$ и $\vert{}\vert{}A^{-1}\vert{}\vert{}_2 = \max \vert{}\lambda(A^{-1})\vert{} = \frac{1}{\min \vert{}\lambda(A)\vert{}}$.
Следовательно:


$$K_2(A) = \frac{\max \vert{}\lambda(A)\vert{}}{\min \vert{}\lambda(A)\vert{}}$$


Если матрица положительно определённая ($A = A^T > 0$), то:


$$K_2(A) = \frac{\lambda_{\max}}{\lambda_{\min}}$$

---

### Пример плохой обусловленности (Система, чувствительная к погрешностям)

Рассмотрим систему треугольного вида:


$$\begin{cases} x_1 - x_2 - x_3 - ... - x_n = b_1 \\ \quad x_2 - x_3 - ... - x_n = b_2 \\ \qquad \ddots \\ \qquad \quad x_{n-1} - x_n = b_{n-1} \\ \qquad \qquad \quad x_n = b_n \end{cases}$$

Алгоритм решения (обратная подстановка):


$$x_n = b_n$$

$$x_i = b_i + \sum_{j=i+1}^n x_j; \quad i = n-1, n-2, ..., 1$$

Возьмём вместо правой части конкретные числа: $b = [-1, -1, ..., -1, 1]^T$.


$$\begin{cases} x_1 - x_2 - x_3 - ... - x_n = -1 \\ \quad x_2 - x_3 - ... - x_n = -1 \\ \qquad \ddots \\ \qquad \quad x_{n-1} - x_n = -1 \\ \qquad \qquad \quad x_n = 1 \end{cases}$$


Точное решение этой системы: $x = [0, 0, ..., 0, 1]^T$.

Пусть теперь мы внесли крошечную ошибку в $x_n$, и посчитали $x_n = 1 + \varepsilon$.
Тогда новое (возмущенное) решение $x^*$ будет вычисляться как:

* $x_{n-1}^* = x_n^* - 1 = (1+\varepsilon) - 1 = \varepsilon$

* $x_{n-2}^* = x_{n-1}^* + x_n^* - 1 = \varepsilon + (1+\varepsilon) - 1 = 2\varepsilon$

* $x_{n-3}^* = x_{n-2}^* + x_{n-1}^* + x_n^* - 1 = 2\varepsilon + \varepsilon + (1+\varepsilon) - 1 = 4\varepsilon = 2^2 \varepsilon$

* ...
* $x_1^* = 2^{n-2} \varepsilon$


Новый вектор решения:


$$x^* = \begin{bmatrix} 2^{n-2}\varepsilon \\ 2^{n-3}\varepsilon \\ ... \\ \varepsilon \\ 1+\varepsilon \end{bmatrix}$$

**Поразительный факт:** Если $n=50$ (всего 50 уравнений), и мы допустили крошечную машинную ошибку $\varepsilon = 2^{-20}$ (около $10^{-6}$).
Тогда $x_1^* = 2^{50-2} \cdot 2^{-20} = 2^{28}$ вместо ожидаемого $0$ 🤯! Ошибка стала катастрофической.

Посчитаем число обусловленности для этого примера:
$\Delta x = x^* - x = \begin{bmatrix} 2^{n-2}\varepsilon \\ 2^{n-3}\varepsilon \\ ... \\ \varepsilon \\ \varepsilon \end{bmatrix}$, исходный $b = \begin{bmatrix} -1 \\ -1 \\ ... \\ -1 \\ 1 \end{bmatrix}$, возмущенный $b^* = \begin{bmatrix} -1 \\ -1 \\ ... \\ -1 \\ 1+\varepsilon \end{bmatrix}$.
Тогда вектор ошибки правой части: $\Delta b = \begin{bmatrix} 0 \\ 0 \\ ... \\ 0 \\ \varepsilon \end{bmatrix}$.

Подставим в формулу обусловленности в $\infty$-норме:


$$K(A) \ge \frac{\frac{\vert{}\vert{}\Delta x\vert{}\vert{}_\infty}{\vert{}\vert{}x\vert{}\vert{}_\infty}}{\frac{\vert{}\vert{}\Delta b\vert{}\vert{}_\infty}{\vert{}\vert{}b\vert{}\vert{}_\infty}} = \frac{\frac{2^{n-1}\varepsilon}{1}}{\frac{\varepsilon}{1}} = 2^{n-1}$$


$\Rightarrow K(A) \ge 2^{n-1}$ $\hookrightarrow$ Это очень большое число обусловленности, система нестабильна.

---

## Полная теорема о возмущениях (Погрешность и в матрице, и в правой части)

Пусть имеем систему $Ax = b$.
Предположим, что погрешность есть не только в векторе $b$, но и в самой матрице $A$:


$$(*)(A + \Delta A)(x + \Delta x) = b + \Delta b$$

Мы изначально считали, что $\det A \neq 0$, но когда возмущенная матрица $A + \Delta A$ может стать вырожденной из-за $\Delta A$?
Будем считать, что:


$$\vert{}\vert{}A^{-1}\Delta A\vert{}\vert{} < 1 \quad (*)_2$$


Это условие гарантирует невырожденность $A+\Delta A$.

*Доказательство невырожденности:*


$$A + \Delta A = A(I + A^{-1}\Delta A)$$

$$\det(A + \Delta A) = \det A \cdot \det(I + A^{-1}\Delta A)$$


Так как $\det A \neq 0$ по условию, проблема может быть только если $\det(I + A^{-1}\Delta A) = 0$.
Но если бы $\det(I + A^{-1}\Delta A) = 0$, тогда:
$\det(\lambda I - (-A^{-1}\Delta A)) = 0$ для $\lambda = -1$, то есть $\lambda = -1$ являлось бы собственным значением для матрицы $A^{-1}\Delta A$.
Но мы предположили, что $\vert{}\vert{}A^{-1}\Delta A\vert{}\vert{} < 1$. А так как спектральный радиус $\rho(A^{-1}\Delta A) \le \vert{}\vert{}A^{-1}\Delta A\vert{}\vert{} < 1$, то собственное значение не может быть равно $-1$ по модулю. Противоречие.

Вернёмся к уравнению $(*)$ и раскроем скобки:


$$Ax + A\Delta x + \Delta A x + \Delta A \Delta x = b + \Delta b$$


Так как $Ax = b$, они сокращаются:


$$(A + \Delta A)\Delta x = -\Delta A x + \Delta b$$


Умножим слева на $(A + \Delta A)^{-1}$:


$$\Delta x = (A + \Delta A)^{-1} [-\Delta A x + \Delta b]$$

Хотим оценить $\Delta x$ через $\Delta b$ и $\Delta A$. Возьмём норму от обеих частей:


$$\vert{}\vert{}\Delta x\vert{}\vert{} \le \vert{}\vert{}(A + \Delta A)^{-1}\vert{}\vert{} \cdot \vert{}\vert{}-\Delta A x + \Delta b\vert{}\vert{} \le \vert{}\vert{}(A + \Delta A)^{-1}\vert{}\vert{} \cdot [\vert{}\vert{}\Delta A\vert{}\vert{} \cdot \vert{}\vert{}x\vert{}\vert{} + \vert{}\vert{}\Delta b\vert{}\vert{}]$$

Искусственно умножим и разделим слагаемое с $\Delta b$ на $\vert{}\vert{}A\vert{}\vert{}\cdot\vert{}\vert{}x\vert{}\vert{}$ (ведь $\vert{}\vert{}b\vert{}\vert{} \le \vert{}\vert{}A\vert{}\vert{}\cdot\vert{}\vert{}x\vert{}\vert{}$):


$$\vert{}\vert{}\Delta x\vert{}\vert{} \le \vert{}\vert{}(A + \Delta A)^{-1}\vert{}\vert{} \cdot \left[\vert{}\vert{}\Delta A\vert{}\vert{} \cdot \vert{}\vert{}x\vert{}\vert{} + \frac{\vert{}\vert{}\Delta b\vert{}\vert{}}{\vert{}\vert{}b\vert{}\vert{}} \vert{}\vert{}A\vert{}\vert{} \cdot \vert{}\vert{}x\vert{}\vert{}\right]$$

Разделим обе части на $\vert{}\vert{}x\vert{}\vert{}$:


$$\frac{\vert{}\vert{}\Delta x\vert{}\vert{}}{\vert{}\vert{}x\vert{}\vert{}} \le \vert{}\vert{}(A + \Delta A)^{-1}\vert{}\vert{} \cdot \vert{}\vert{}A\vert{}\vert{} \cdot \left[\frac{\vert{}\vert{}\Delta A\vert{}\vert{}}{\vert{}\vert{}A\vert{}\vert{}} + \frac{\vert{}\vert{}\Delta b\vert{}\vert{}}{\vert{}\vert{}b\vert{}\vert{}}\right]$$

Теперь нам нужно оценить $\vert{}\vert{}(A + \Delta A)^{-1}\vert{}\vert{}$.
Используем представление $A + \Delta A = A(I + A^{-1}\Delta A)$.
Тогда $(A + \Delta A)^{-1} = (I + A^{-1}\Delta A)^{-1} A^{-1}$.
Берём норму:


$$\vert{}\vert{}(A + \Delta A)^{-1}\vert{}\vert{} \le \vert{}\vert{}(I + A^{-1}\Delta A)^{-1}\vert{}\vert{} \cdot \vert{}\vert{}A^{-1}\vert{}\vert{}$$

Подставляем это в наше неравенство:


$$\frac{\vert{}\vert{}\Delta x\vert{}\vert{}}{\vert{}\vert{}x\vert{}\vert{}} \le \vert{}\vert{}(I + A^{-1}\Delta A)^{-1}\vert{}\vert{} \cdot \underbrace{\vert{}\vert{}A^{-1}\vert{}\vert{} \cdot \vert{}\vert{}A\vert{}\vert{}}_{K(A)} \left[\frac{\vert{}\vert{}\Delta A\vert{}\vert{}}{\vert{}\vert{}A\vert{}\vert{}} + \frac{\vert{}\vert{}\Delta b\vert{}\vert{}}{\vert{}\vert{}b\vert{}\vert{}}\right]$$

Для оценки первой скобки вспомним **ряд Неймана**: $\sum_{k=0}^\infty M^k = (I - M)^{-1}$.
Подставим $M = -A^{-1}\Delta A$:


$$(I + A^{-1}\Delta A)^{-1} = \sum_{k=0}^\infty (-A^{-1}\Delta A)^k$$


Ряд сходится, так как достаточное условие сходимости $\rho \le \vert{}\vert{}A^{-1}\Delta A\vert{}\vert{} < 1$ выполнено (наше условие $(*)_2$).

Берём норму от суммы ряда (используем формулу суммы бесконечно убывающей геометрической прогрессии):


$$\left\vert{}\left\vert{} \sum_{k=0}^\infty (-A^{-1}\Delta A)^k \right\vert{}\right\vert{} \le \sum_{k=0}^\infty \vert{}\vert{}A^{-1}\Delta A\vert{}\vert{}^k = \frac{1}{1 - \vert{}\vert{}A^{-1}\Delta A\vert{}\vert{}}$$

Собираем всё вместе в итоговую формулу оценки относительной погрешности:


$$\frac{\vert{}\vert{}\Delta x\vert{}\vert{}}{\vert{}\vert{}x\vert{}\vert{}} \le \frac{K(A)}{1 - \vert{}\vert{}A^{-1}\Delta A\vert{}\vert{}} \left[ \frac{\vert{}\vert{}\Delta A\vert{}\vert{}}{\vert{}\vert{}A\vert{}\vert{}} + \frac{\vert{}\vert{}\Delta b\vert{}\vert{}}{\vert{}\vert{}b\vert{}\vert{}} \right]$$

> 💡 **Объяснение:** Эта грандиозная итоговая формула — венец теории возмущений для линейных систем. Она показывает, что итоговая ошибка решения ($\frac{\vert{}\vert{}\Delta x\vert{}\vert{}}{\vert{}\vert{}x\vert{}\vert{}}$) ограничена суммой относительных ошибок матрицы ($\frac{\vert{}\vert{}\Delta A\vert{}\vert{}}{\vert{}\vert{}A\vert{}\vert{}}$) и вектора ($\frac{\vert{}\vert{}\Delta b\vert{}\vert{}}{\vert{}\vert{}b\vert{}\vert{}}$), умноженной на гигантский "усилитель". Этим усилителем выступает число обусловленности $K(A)$, слегка скорректированное знаменателем $1 - \vert{}\vert{}A^{-1}\Delta A\vert{}\vert{}$. Если $K(A)$ велико, то даже минимальные неточности в матрице или правой части взорвут ошибку ответа до небес.