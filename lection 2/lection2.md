# Решение систем линейных алгебраических уравнений

Дана система уравнений:

$$\begin{cases} a_{11}x_1 + a_{12}x_2 + ... + a_{1n}x_n = b_1 \\ a_{21}x_1 + a_{22}x_2 + ... + a_{2n}x_n = b_2 \\ ... \\ a_{n1}x_1 + a_{n2}x_2 + ... + a_{nn}x_n = b_n \end{cases}$$

Предполагаем, что $a_{ij}, b_i \in \mathbb{R}$.

Пусть матрицы имеют вид:


$$A = \begin{bmatrix} a_{11} & ... & a_{1n} \\ a_{21} & ... & a_{2n} \\ ... & ... & ... \\ a_{n1} & ... & a_{nn} \end{bmatrix}_{n \times n}; \quad b = \begin{bmatrix} b_1 \\ ... \\ b_n \end{bmatrix}_{n \times 1}; \quad x = \begin{bmatrix} x_1 \\ ... \\ x_n \end{bmatrix}_{n \times 1}$$

(1) перепишем в виде:

**$Ax = b$** (2)

Если $\det A \neq 0$, то система (1) / уравн. (2) имеет единственное решение: $x = A^{-1}b$. Но вычислить обратную матрицу $A^{-1}$ трудно. Поэтому нужен этот новый метод.

**Формулы Крамера:**


$$x_i = \frac{\Delta_i}{\Delta}; \quad i = 1, n$$


где $\Delta = \det A$, а $\Delta_i$ — определитель, получающийся из $\Delta$ путём замены его $i$-го столбца столбцом свободных членов системы.

Для вычисления необходимо операций:


$$A_{ops} = (n+1)! \text{ (умнож.)} + n! - 1 \text{ (слож.)} = n \cdot n! - 1$$


Этот способ неэффективный.

> 💡 **Объяснение:** Метод Крамера требует вычисления $(n+1)$ определителей. Поиск определителя по определению — это факториал $\mathcal{O}(n!)$. Для матрицы 20x20 это число настолько огромно, что даже суперкомпьютеру потребуются тысячелетия. Поэтому на практике метод Крамера для больших систем никогда не используется.

### Методы решения



**Прямые:**

* Решение за конечное число арифметических действий.


* Вычислительные погрешности неизбежны.



**Итерационные:**

* Последовательные приближения.


* Имеем $x^*$. Выбирается начальное $x_0$.


* Каким-то правилом: $x_1 \to x_2 \to ...$

* В результате приближаемся к решению.



---

## Системы, решаемые прямым методом



**1. Диагональная**

$$A = \begin{bmatrix} a_{11} & 0 & ... & 0 \\ 0 & a_{22} & ... & 0 \\ ... & ... & ... & ... \\ 0 & 0 & ... & a_{nn} \end{bmatrix}$$


Если $a_{ii} \neq 0, \ i=\overline{1,n}$, то решение:


$$x_i = \frac{b_i}{a_{ii}}; \quad i = \overline{1,n}$$


Число операций: $A_{ops} = n$.

**2. Треугольная**

$$A = \begin{bmatrix} a_{11} & a_{12} & ... & a_{1n} \\ 0 & a_{22} & ... & a_{2n} \\ ... & ... & ... & ... \\ 0 & 0 & ... & a_{nn} \end{bmatrix}$$


Если $a_{ii} \neq 0, \ i=\overline{1,n}$:


$$x_n = \frac{b_n}{a_{nn}}$$

$$x_i = \frac{1}{a_{ii}} \left( b_i - \sum_{j=i+1}^n a_{ij} x_j \right); \quad i = n-1, ..., 1$$


Оценим число операций ($A_{ops}$):


$$A_{ops} = \sum_{i=1}^n \left( \underbrace{n - (i+1) + 1}_{\text{умножения}} + \underbrace{n - (i+1) + 1}_{\text{сложения}} + \underbrace{1}_{\text{деление}} \right) = \sum_{i=1}^n (2(n-i) + 1) = 2(1 + 2 + ... + n - 1) + n = 2 \cdot \frac{1 + n - 1}{2} (n - 1) + n = n(n-1) + n = n^2$$

---

## Сведения из линейной алгебры



Рассм. векторное пространство $\mathbb{R}^n$ ($\mathbb{C}^n$).
Пусть имеем 2 вектора:


$$x = \begin{bmatrix} x_1 \\ x_2 \\ ... \\ x_n \end{bmatrix} \quad \text{и} \quad y = \begin{bmatrix} y_1 \\ y_2 \\ ... \\ y_n \end{bmatrix}$$

**Опр.** Скалярное произведение двух векторов в $\mathbb{R}^n$:


$$(x, y) = \sum_{i=1}^n x_i y_i$$

**Свойства:**

1. $(x, x) \ge 0, \quad (x, x) = 0 \iff x = 0$

2. $(x, y) = (y, x)$

3. $(x+y, z) = (x, z) + (y, z)$

4. $(\alpha x, y) = \alpha(x, y)$


**Опр.** Скалярное произведение двух векторов в $\mathbb{C}^n$:


$$(x, y) = \sum_{i=1}^n x_i \overline{y}_i$$

*Почему сопряженное? Чтобы сохранить свойство 1*.

**Свойства в $\mathbb{C}^n$:**

1. $(x, x) = \sum_{i=1}^n x_i \overline{x}_i = \sum_{i=1}^n \vert{}x_i\vert{}^2 \ge 0, \quad (x, x) = 0 \iff x = 0$

2. $(x, y) = \overline{(y, x)}$

3. $(x+y, z) = (x, z) + (y, z)$

4. $(\alpha x, y) = \alpha(x, y)$


Рассм. ещё одно свойство (когда скаляр у второго аргумента):
В $\mathbb{R}^n$: $(x, \alpha y) \stackrel{2)}{=} (\alpha y, x) \stackrel{4)}{=} \alpha(y, x) \stackrel{2)}{=} \alpha(x, y); \quad \alpha \in \mathbb{R}$
В $\mathbb{C}^n$: $(x, \alpha y) \stackrel{2)}{=} \overline{(\alpha y, x)} \stackrel{4)}{=} \overline{\alpha(y, x)} \stackrel{2)}{=} \overline{\alpha} \cdot \overline{(y, x)} = \overline{\alpha} \cdot (x, y)$

**Опр.** Если $(x, y) = 0$, то векторы $x$ и $y$ **ортогональны**.
**Опр.** Если $(x, y) = 1$, то векторы $x$ и $y$ **нормированны**. *(Примечание: обычно нормированность означает $(x,x)=1$, на лекции записано $(x,y)=1$, возможно опечатка преподавателя)*.

**Неравенство Коши-Буняковского:**

$$\vert{}(x, y)\vert{} \le \sqrt{(x, x)}\sqrt{(y, y)}, \quad \forall x, y \in \mathbb{C}^n$$

**Опр.** Система векторов ортогональна, если либо она состоит из 1 вектора, либо её векторы попарно ортогональны.
Ортогональная система нормированных векторов называется **ортонормированной**.

---

## Собственные значения и собственные векторы



Пусть имеем $A = [a_{ij}]_{n \times n} \in \mathbb{R}^{n \times n}$.

**Опр.** Число $\lambda$ — **собственное значение** матрицы $A$, если $\exists x \neq 0$ ; $Ax = \lambda x$, причём $x$ — **собственный вектор**.

**Пример:**

$$A = \begin{bmatrix} 2 & 3 \\ 1 & 2 \end{bmatrix} \quad \begin{vmatrix} 2-\lambda & 3 \\ 1 & 2-\lambda \end{vmatrix} = 0 = (2-\lambda)^2 - 3$$

**Опр.** Число $\lambda$ — собств. зн. $A \iff \det(\lambda I - A) = 0$.

**Опр.** Совокупность всех собственных значений называется **спектром матрицы** $\equiv \text{sp } A$.

$$\det(\lambda I - A) = \begin{vmatrix} \lambda - a_{11} & -a_{12} & ... & -a_{1n} \\ -a_{21} & \lambda - a_{22} & ... & -a_{2n} \\ ... & ... & ... & ... \\ -a_{n1} & -a_{n2} & ... & \lambda - a_{nn} \end{vmatrix} = \lambda^n - p_1 \lambda^{n-1} + p_2 \lambda^{n-2} - ... + (-1)^n p_n \equiv P(\lambda) \text{ — характеристический многочлен.}$$

**Опр.** Определитель $k$-го порядка, составленный из элементов матрицы $A$, стоящих на пересечении строк с номерами $i_1 ... i_k$ и столбцов с номерами $j_1 ... j_k$, называется **минором $k$-го порядка** $\equiv A \binom{i_1 \ i_2 \ ... \ i_k}{j_1 \ j_2 \ ... \ j_k}$.

* $A \binom{i_1 \ i_2 \ ... \ i_k}{i_1 \ i_2 \ ... \ i_k}$ — **главный минор**.


* $A \binom{1 \ 2 \ ... \ k}{1 \ 2 \ ... \ k}$ — **угловой минор**.



Оказывается, что:


$$p_k = \sum_{1 \le i_1 < ... < i_k \le n} A \binom{i_1 \ i_2 \ ... \ i_k}{i_1 \ i_2 \ ... \ i_k}; \quad k = \overline{1, n}$$


В частности (1):


$$p_1 = \sum_{i=1}^n a_{ii} = \text{tr } A \quad (\text{trace - след})$$

$$p_n = \det A$$

С другой стороны:


$$P(\lambda) = (\lambda - \lambda_1)(\lambda - \lambda_2)...(\lambda - \lambda_n) = \lambda^n - \left(\sum_{i=1}^n \lambda_i\right) \cdot \lambda^{n-1} + ... + (-1)^n \left(\prod_{i=1}^n \lambda_i\right)$$


Т.е. (2):


$$p_1 = \sum_{i=1}^n \lambda_i$$

$$p_n = \prod_{i=1}^n \lambda_i$$

Из (1) и (2) следует **(теорема Виета)**:


$$\sum_{i=1}^n \lambda_i = \text{tr } A$$

$$\prod_{i=1}^n \lambda_i = \det A$$

Если матрица невырожденная ($\det A \neq 0$), то все её собственные значения ненулевые.

* **Лемма 1.** Для того, чтобы число $\lambda=0$ являлось собственным значением $A$, необх. и дост., чтобы $\det A = 0$.


* **Лемма 2.** Собственные значения матриц $A$ и $A^T$ совпадают.



Рассм. действительные матрицы, но комплексные векторы, т.к. собств. значения действ-х матриц могут быть комплексными.

**Пример:**

$$A = \begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix}$$

$$\det(\lambda I - A) = \begin{vmatrix} \lambda - 1 & -1 \\ 1 & \lambda - 1 \end{vmatrix} = 0$$

$$(\lambda - 1)^2 + 1 = 0 \Rightarrow (\lambda - 1)^2 = -1 \Rightarrow \lambda - 1 = \pm i \Rightarrow \lambda = 1 \pm i \in \mathbb{C}$$


Имеем $Ax = \lambda x$ (матрица $A \in \mathbb{R}$, вектор $x \in \mathbb{C}^n$, $\lambda \in \mathbb{C}$).

**Свойство 5)** $(Ax, y) = (x, A^T y)$ (док. для $\mathbb{R}^n$)
*Доказательство:*


$$(x, y) = \sum_{i=1}^n x_i y_i = [y_1, ..., y_n] \cdot \begin{bmatrix} x_1 \\ ... \\ x_n \end{bmatrix} = y^T x$$


Тогда:
$(Ax, y) = y^T (Ax)$
$(x, A^T y) = (A^T y)^T \cdot x = y^T A x$
Левые части равны, следовательно, свойство доказано $\blacksquare$.

В характеристическом многочлене $P(\lambda) = (\lambda - \lambda_1)(\lambda - \lambda_2)...(\lambda - \lambda_n) \equiv$


Пусть $\lambda_1, ..., \lambda_k$ — попарно различные собств. значения.
$\equiv (\lambda - \lambda_1)^{\alpha_1} \cdot (\lambda - \lambda_2)^{\alpha_2} \cdot ... \cdot (\lambda - \lambda_k)^{\alpha_k}$, где $\alpha_1 + \alpha_2 + ... + \alpha_k = n$.
$\alpha_i$ — кратность $\lambda_i$.

### Примеры нахождения собственных значений и векторов:

**1.** $I = \begin{bmatrix} 1 & 0 & ... & 0 \\ 0 & 1 & ... & 0 \\ ... & ... & ... & ... \\ 0 & 0 & ... & 1 \end{bmatrix}_{n \times n}$


$\det(\lambda I - I) = \det(I(\lambda - 1)) = \begin{bmatrix} \lambda-1 & & 0 \\ & ... & \\ 0 & & \lambda-1 \end{bmatrix} = (\lambda - 1)^n = 0 \Rightarrow \lambda = 1$


Собств. зн. $\lambda = 1$.
Собств. векторы $x$: $Ix = x$, т.е. $x - \forall \neq 0$ вектор.

**2.** $A = \begin{bmatrix} 1 & 1 & ... & 1 \\ 1 & 1 & ... & 1 \\ 1 & 1 & ... & 1 \end{bmatrix}_{n \times n}$

$$\det(\lambda I - A) = \lambda^n - n\lambda^{n-1} = \lambda^{n-1} (\lambda - n) = 0$$


Получаем:
$\lambda_1 = n$ (кратность 1)
$\lambda_2 = 0$ (кратность $n-1$)

*Найдём векторы:*
**2.1.** Для $\lambda_1 = n$:
$Ax = n x$


$$\begin{cases} x_1 + x_2 + ... + x_n = n x_1 \\ ... \\ x_1 + x_2 + ... + x_n = n x_n \end{cases} \Rightarrow x = e = \begin{bmatrix} 1 \\ ... \\ 1 \end{bmatrix}_{n \times 1}$$

**2.2.** Для $\lambda_2 = 0$:
$Ax = 0 \cdot x \Rightarrow Ax = 0$


$$\begin{cases} x_1 + x_2 + ... + x_n = 0 \\ ... \\ x_1 + x_2 + ... + x_n = 0 \end{cases}$$


Следовательно, любой вектор $x = \begin{bmatrix} x_1 \\ ... \\ x_n \end{bmatrix} \neq 0$, удовлетворяющий $\sum_{i=1}^n x_i = 0$, является собственным.

---

## Симметричные и положительно определённые матрицы



**Опр.** Матрица называется **симметричной**, если $A = A^T$; $A \in \mathbb{R}^{n \times n}$.

**Лемма.** Собственные значения симметричных матриц являются действительными числами.

**Теорема (Отношение Рэлея):**


Пусть $A \in \mathbb{R}^{n \times n}$ — симметричная матрица.
Тогда $\forall x \in \mathbb{R}^n; x \neq 0$:


$$\lambda_{min} \le \frac{(Ax, x)}{(x, x)} \le \lambda_{max}$$


где $\lambda_{min}$ и $\lambda_{max}$ — минимальное и максимальное из собств. значений $A$.
Более того:


$$\lambda_{min} = \min_{x \neq 0} \frac{(Ax, x)}{(x, x)}, \quad \lambda_{max} = \max_{x \neq 0} \frac{(Ax, x)}{(x, x)}$$


Дробь $\frac{(Ax, x)}{(x, x)}$ называется **отношением Рэлея**.

> 💡 **Объяснение:** Отношение Рэлея — это мощный инструмент для оценки собственных значений. Геометрически, если мы возьмём любой ненулевой вектор $x$, умножим его на матрицу $A$, и спроецируем результат обратно на $x$ (через скалярное произведение), а затем отнормируем, то полученное число *всегда* будет зажато между самым маленьким и самым большим собственным значением матрицы.

**Доказательство:**


Так как матрица симметричная, её собственные векторы $e_1, ..., e_n$ образуют ортонормированный базис: $(e_i, e_j) = \delta_{ij}$ (символ Кронекера). Разложим вектор $x$ по этому базису: $x = \sum \alpha_i e_i$.

Вычислим скалярные произведения:


$$(x, x) = \left(\sum_{i=1}^n \alpha_i e_i, \sum_{j=1}^n \alpha_j e_j\right) = \sum_{i=1}^n \sum_{j=1}^n \alpha_i \alpha_j (e_i, e_j) = \sum_{i=1}^n \alpha_i^2$$

$$(Ax, x) = \left(\sum_{i=1}^n \alpha_i \lambda_i e_i, \sum_{j=1}^n \alpha_j e_j\right) = \sum_{i=1}^n \sum_{j=1}^n \alpha_i \alpha_j \lambda_i (e_i, e_j) = \sum_{i=1}^n \lambda_i \alpha_i^2$$

Так как $\lambda_{min} \le \lambda_i \le \lambda_{max}$, оценим сумму:


$$\lambda_{min}(x, x) = \lambda_{min} \sum_{i=1}^n \alpha_i^2 \le (Ax, x) \le \lambda_{max} \sum_{i=1}^n \alpha_i^2 = \lambda_{max}(x, x)$$


Т.е., поделив на $(x,x) > 0$, получаем:


$$\lambda_{min} \le \frac{(Ax, x)}{(x, x)} \le \lambda_{max}$$

Покажем, что $\exists$ вектор, при котором достигается равенство. Подставим $x = e_1$ (вектор, соответствующий $\lambda_{min}$):


$$\frac{(Ae_1, e_1)}{(e_1, e_1)} = \frac{(\lambda_1 e_1, e_1)}{(e_1, e_1)} = \lambda_1 \frac{(e_1, e_1)}{(e_1, e_1)} = \lambda_1 = \lambda_{min}$$


Аналогично для $\lambda_{max}$, если подставить вектор, соответствующий $\lambda_{max}$. $\blacksquare$

**Опр.** Симметричная матрица $A$ называется **положительно определённой** и записывается $A > 0$, если $(Ax, x) > 0 \quad \forall x \neq 0 \in \mathbb{R}^n$.
**Положительно полуопределённой**, если $(Ax, x) \ge 0; \ A \ge 0 \quad \forall x \in \mathbb{R}^n$.

**Примеры:**
**1.** $A = \begin{bmatrix} 1 & 1 \\ 1 & 2 \end{bmatrix} \quad x = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \quad Ax = \begin{bmatrix} x_1 + x_2 \\ x_1 + 2x_2 \end{bmatrix}$

$$(Ax, x) = x_1(x_1 + x_2) + x_2(x_1 + 2x_2) = x_1^2 + 2x_1 x_2 + 2x_2^2 = (x_1 + x_2)^2 + x_2^2 > 0$$


Вывод: $A > 0$.

**2.** $A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} \quad x = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \quad Ax = \begin{bmatrix} x_1 + x_2 \\ x_1 + x_2 \end{bmatrix}$

$$(Ax, x) = x_1^2 + 2x_1 x_2 + x_2^2 = (x_1 + x_2)^2 \ge 0$$


Вывод: $A \ge 0$.
Если $A = 0 \Rightarrow x_1 = -x_2$, например $x = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$ или $x = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$ и т.д.

**Лемма.** Собственные значения положительно определённой матрицы положительны, а положительно полуопределённой — неотрицательны.


$$0 \le (Ax, x) = (\lambda x, x) = \lambda \underbrace{(x, x)}_{>0} \Rightarrow \lambda \ge 0$$

**Критерий Сильвестра:**


Для того, чтобы матрица $A$ была положительно определённой, необходимо и достаточно, чтобы все её угловые миноры были положительными.


$$A > 0 \quad ((Ax, x) > 0) \iff A \binom{1 \ 2 \ ... \ k}{1 \ 2 \ ... \ k} > 0 \quad \forall k = \overline{1, n}$$

**Для $A > 0$ справедливо:**

1. $\det A \neq 0$

2. диагональные элементы $a_{ii} > 0; \ i = \overline{1, n}$

3. $A^{-1} > 0$


**Опр.** Матрицы $A$ и $B$ **подобные**, если $\exists S; \det S \neq 0$:


$$A = S^{-1}BS \iff B = SAS^{-1}$$

 *(Примечание: в конспекте написано $A = S^{-1}BS \iff B = SAS^{-1}$, это стандартное определение подобия)*.

**Лемма.** Собственные значения подобных матриц совпадают.
*Доказательство:*


$$\det(\lambda I - A) = \det(\lambda I - S^{-1}BS) = \det(S^{-1}(\lambda I - B)S) = \det S^{-1} \cdot \det(\lambda I - B) \cdot \det S = \det(\lambda I - B)$$


Характеристические многочлены равны, значит их корни (собственные значения) совпадают.

---

## Нормы векторов и матриц



Рассм. $\mathbb{C}^n$.

**Опр.** Нормой вектора $x \in \mathbb{C}^n$ называется вещественное число:

1. $\vert{}\vert{}x\vert{}\vert{} \ge 0, \quad \vert{}\vert{}x\vert{}\vert{} = 0 \iff x = 0$

2. $\vert{}\vert{}\alpha x\vert{}\vert{} = \vert{}\alpha\vert{} \cdot \vert{}\vert{}x\vert{}\vert{}$

3. $\vert{}\vert{}x + y\vert{}\vert{} \le \vert{}\vert{}x\vert{}\vert{} + \vert{}\vert{}y\vert{}\vert{}$ (неравенство треугольника)



**Способы введения нормы в пространство:**

* **$l_\infty$ (кубическая):** $\vert{}\vert{}x\vert{}\vert{}_\infty \equiv \max_{1 \le i \le n} \vert{}x_i\vert{}$

* **$l_1$ (октаэдрическая):** $\vert{}\vert{}x\vert{}\vert{}_1 \equiv \sum_{i=1}^n \vert{}x_i\vert{}$

* **$l_2$ (сферическая/евклидова):** $\vert{}\vert{}x\vert{}\vert{}_2 \equiv \left( \sum_{i=1}^n \vert{}x_i\vert{}^2 \right)^{\frac{1}{2}}$


Это частные случаи **нормы Гёльдера $l_p$**:

$$\vert{}\vert{}x\vert{}\vert{}_p = \left( \sum_{i=1}^n \vert{}x_i\vert{}^p \right)^{\frac{1}{p}}; \quad p \ge 1$$

Оценим:


$$\max_{1 \le i \le n} \vert{}x_i\vert{} = \left( \max_{1 \le i \le n} \vert{}x_i\vert{}^p \right)^{\frac{1}{p}} \le \left( \sum_{i=1}^n \vert{}x_i\vert{}^p \right)^{\frac{1}{p}} \le \left( n \max_{1 \le i \le n} \vert{}x_i\vert{}^p \right)^{\frac{1}{p}} = n^{\frac{1}{p}} \max_{1 \le i \le n} \vert{}x_i\vert{}$$


При $p \to \infty \Rightarrow n^{1/p} \to 1$, следовательно $\left( \sum \vert{}x_i\vert{}^p \right)^{1/p} \to \max_{1 \le i \le n} \vert{}x_i\vert{} =: l_\infty$, поэтому и используется значок $\infty$.

Связь $l_2$ нормы со скалярным произведением:


$$\vert{}\vert{}x\vert{}\vert{}_2 = \left( \sum_{i=1}^n \vert{}x_i\vert{}^2 \right)^{\frac{1}{2}}$$

$$(x, x) = \sum_{i=1}^n \vert{}x_i\vert{}^2$$


Следовательно: $\vert{}\vert{}x\vert{}\vert{}_2 = \sqrt{(x, x)}$.

**Опр.** Нормой матрицы $A \in \mathbb{C}^{n \times n}$ называется вещественное число $\vert{}\vert{}A\vert{}\vert{}$:

1. $\vert{}\vert{}A\vert{}\vert{} \ge 0, \quad \vert{}\vert{}A\vert{}\vert{} = 0 \iff A = 0$

2. $\vert{}\vert{}\alpha A\vert{}\vert{} = \vert{}\alpha\vert{} \cdot \vert{}\vert{}A\vert{}\vert{}, \quad \forall \alpha \in \mathbb{C}$

3. $\vert{}\vert{}A + B\vert{}\vert{} \le \vert{}\vert{}A\vert{}\vert{} + \vert{}\vert{}B\vert{}\vert{}$

Вот продолжение твоего конспекта, переведённое в Markdown. Я тщательно перенёс все формулы, доказательства и примеры с приложенных фотографий.

Так как на этих страницах нет графиков функций (только формулы, матрицы и несколько поясняющих одномерных осей), скрипт на Python для генерации картинок в этот раз не понадобится. Весь материал отлично рендерится средствами самого LaTeX.

Как и в прошлый раз, я добавил блоки с объяснениями для самых важных и сложных концепций.

---

# Решение систем линейных алгебраических уравнений

Дана система уравнений:

$$\begin{cases} a_{11}x_1 + a_{12}x_2 + ... + a_{1n}x_n = b_1 \\ a_{21}x_1 + a_{22}x_2 + ... + a_{2n}x_n = b_2 \\ ... \\ a_{n1}x_1 + a_{n2}x_2 + ... + a_{nn}x_n = b_n \end{cases}$$

Предполагаем, что $a_{ij}, b_i \in \mathbb{R}$.

Пусть матрицы имеют вид:


$$A = \begin{bmatrix} a_{11} & ... & a_{1n} \\ a_{21} & ... & a_{2n} \\ ... & ... & ... \\ a_{n1} & ... & a_{nn} \end{bmatrix}_{n \times n}; \quad b = \begin{bmatrix} b_1 \\ ... \\ b_n \end{bmatrix}_{n \times 1}; \quad x = \begin{bmatrix} x_1 \\ ... \\ x_n \end{bmatrix}_{n \times 1}$$

(1) перепишем в виде:

**$Ax = b$** (2)

Если $\det A \neq 0$, то система (1) / уравн. (2) имеет единственное решение: $x = A^{-1}b$. Но вычислить обратную матрицу $A^{-1}$ трудно. Поэтому нужен этот новый метод.

**Формулы Крамера:**


$$x_i = \frac{\Delta_i}{\Delta}; \quad i = 1, n$$


где $\Delta = \det A$, а $\Delta_i$ — определитель, получающийся из $\Delta$ путём замены его $i$-го столбца столбцом свободных членов системы.

Для вычисления необходимо операций:


$$A_{ops} = (n+1)! \text{ (умнож.)} + n! - 1 \text{ (слож.)} = n \cdot n! - 1$$


Этот способ неэффективный.

> 💡 **Объяснение:** Метод Крамера требует вычисления $(n+1)$ определителей. Поиск определителя по определению — это факториал $\mathcal{O}(n!)$. Для матрицы 20x20 это число настолько огромно, что даже суперкомпьютеру потребуются тысячелетия. Поэтому на практике метод Крамера для больших систем никогда не используется.

### Методы решения



**Прямые:**

* Решение за конечное число арифметических действий.


* Вычислительные погрешности неизбежны.



**Итерационные:**

* Последовательные приближения.


* Имеем $x^*$. Выбирается начальное $x_0$.


* Каким-то правилом: $x_1 \to x_2 \to ...$

* В результате приближаемся к решению.



---

## Системы, решаемые прямым методом



**1. Диагональная**

$$A = \begin{bmatrix} a_{11} & 0 & ... & 0 \\ 0 & a_{22} & ... & 0 \\ ... & ... & ... & ... \\ 0 & 0 & ... & a_{nn} \end{bmatrix}$$


Если $a_{ii} \neq 0, \ i=\overline{1,n}$, то решение:


$$x_i = \frac{b_i}{a_{ii}}; \quad i = \overline{1,n}$$


Число операций: $A_{ops} = n$.

**2. Треугольная**

$$A = \begin{bmatrix} a_{11} & a_{12} & ... & a_{1n} \\ 0 & a_{22} & ... & a_{2n} \\ ... & ... & ... & ... \\ 0 & 0 & ... & a_{nn} \end{bmatrix}$$


Если $a_{ii} \neq 0, \ i=\overline{1,n}$:


$$x_n = \frac{b_n}{a_{nn}}$$

$$x_i = \frac{1}{a_{ii}} \left( b_i - \sum_{j=i+1}^n a_{ij} x_j \right); \quad i = n-1, ..., 1$$


Оценим число операций ($A_{ops}$):


$$A_{ops} = \sum_{i=1}^n \left( \underbrace{n - (i+1) + 1}_{\text{умножения}} + \underbrace{n - (i+1) + 1}_{\text{сложения}} + \underbrace{1}_{\text{деление}} \right) = \sum_{i=1}^n (2(n-i) + 1) = 2(1 + 2 + ... + n - 1) + n = 2 \cdot \frac{1 + n - 1}{2} (n - 1) + n = n(n-1) + n = n^2$$

---

## Сведения из линейной алгебры



Рассм. векторное пространство $\mathbb{R}^n$ ($\mathbb{C}^n$).
Пусть имеем 2 вектора:


$$x = \begin{bmatrix} x_1 \\ x_2 \\ ... \\ x_n \end{bmatrix} \quad \text{и} \quad y = \begin{bmatrix} y_1 \\ y_2 \\ ... \\ y_n \end{bmatrix}$$

**Опр.** Скалярное произведение двух векторов в $\mathbb{R}^n$:


$$(x, y) = \sum_{i=1}^n x_i y_i$$

**Свойства:**

1. $(x, x) \ge 0, \quad (x, x) = 0 \iff x = 0$

2. $(x, y) = (y, x)$

3. $(x+y, z) = (x, z) + (y, z)$

4. $(\alpha x, y) = \alpha(x, y)$


**Опр.** Скалярное произведение двух векторов в $\mathbb{C}^n$:


$$(x, y) = \sum_{i=1}^n x_i \overline{y}_i$$

*Почему сопряженное? Чтобы сохранить свойство 1*.

**Свойства в $\mathbb{C}^n$:**

1. $(x, x) = \sum_{i=1}^n x_i \overline{x}_i = \sum_{i=1}^n \vert{}x_i\vert{}^2 \ge 0, \quad (x, x) = 0 \iff x = 0$

2. $(x, y) = \overline{(y, x)}$

3. $(x+y, z) = (x, z) + (y, z)$

4. $(\alpha x, y) = \alpha(x, y)$


Рассм. ещё одно свойство (когда скаляр у второго аргумента):
В $\mathbb{R}^n$: $(x, \alpha y) \stackrel{2)}{=} (\alpha y, x) \stackrel{4)}{=} \alpha(y, x) \stackrel{2)}{=} \alpha(x, y); \quad \alpha \in \mathbb{R}$
В $\mathbb{C}^n$: $(x, \alpha y) \stackrel{2)}{=} \overline{(\alpha y, x)} \stackrel{4)}{=} \overline{\alpha(y, x)} \stackrel{2)}{=} \overline{\alpha} \cdot \overline{(y, x)} = \overline{\alpha} \cdot (x, y)$

**Опр.** Если $(x, y) = 0$, то векторы $x$ и $y$ **ортогональны**.
**Опр.** Если $(x, y) = 1$, то векторы $x$ и $y$ **нормированны**. *(Примечание: обычно нормированность означает $(x,x)=1$, на лекции записано $(x,y)=1$, возможно опечатка преподавателя)*.

**Неравенство Коши-Буняковского:**

$$\vert{}(x, y)\vert{} \le \sqrt{(x, x)}\sqrt{(y, y)}, \quad \forall x, y \in \mathbb{C}^n$$

**Опр.** Система векторов ортогональна, если либо она состоит из 1 вектора, либо её векторы попарно ортогональны.
Ортогональная система нормированных векторов называется **ортонормированной**.

---

## Собственные значения и собственные векторы



Пусть имеем $A = [a_{ij}]_{n \times n} \in \mathbb{R}^{n \times n}$.

**Опр.** Число $\lambda$ — **собственное значение** матрицы $A$, если $\exists x \neq 0$ ; $Ax = \lambda x$, причём $x$ — **собственный вектор**.

**Пример:**

$$A = \begin{bmatrix} 2 & 3 \\ 1 & 2 \end{bmatrix} \quad \begin{vmatrix} 2-\lambda & 3 \\ 1 & 2-\lambda \end{vmatrix} = 0 = (2-\lambda)^2 - 3$$

**Опр.** Число $\lambda$ — собств. зн. $A \iff \det(\lambda I - A) = 0$.

**Опр.** Совокупность всех собственных значений называется **спектром матрицы** $\equiv \text{sp } A$.

$$\det(\lambda I - A) = \begin{vmatrix} \lambda - a_{11} & -a_{12} & ... & -a_{1n} \\ -a_{21} & \lambda - a_{22} & ... & -a_{2n} \\ ... & ... & ... & ... \\ -a_{n1} & -a_{n2} & ... & \lambda - a_{nn} \end{vmatrix} = \lambda^n - p_1 \lambda^{n-1} + p_2 \lambda^{n-2} - ... + (-1)^n p_n \equiv P(\lambda) \text{ — характеристический многочлен.}$$

**Опр.** Определитель $k$-го порядка, составленный из элементов матрицы $A$, стоящих на пересечении строк с номерами $i_1 ... i_k$ и столбцов с номерами $j_1 ... j_k$, называется **минором $k$-го порядка** $\equiv A \binom{i_1 \ i_2 \ ... \ i_k}{j_1 \ j_2 \ ... \ j_k}$.

* $A \binom{i_1 \ i_2 \ ... \ i_k}{i_1 \ i_2 \ ... \ i_k}$ — **главный минор**.


* $A \binom{1 \ 2 \ ... \ k}{1 \ 2 \ ... \ k}$ — **угловой минор**.



Оказывается, что:


$$p_k = \sum_{1 \le i_1 < ... < i_k \le n} A \binom{i_1 \ i_2 \ ... \ i_k}{i_1 \ i_2 \ ... \ i_k}; \quad k = \overline{1, n}$$


В частности (1):


$$p_1 = \sum_{i=1}^n a_{ii} = \text{tr } A \quad (\text{trace - след})$$

$$p_n = \det A$$

С другой стороны:


$$P(\lambda) = (\lambda - \lambda_1)(\lambda - \lambda_2)...(\lambda - \lambda_n) = \lambda^n - \left(\sum_{i=1}^n \lambda_i\right) \cdot \lambda^{n-1} + ... + (-1)^n \left(\prod_{i=1}^n \lambda_i\right)$$


Т.е. (2):


$$p_1 = \sum_{i=1}^n \lambda_i$$

$$p_n = \prod_{i=1}^n \lambda_i$$

Из (1) и (2) следует **(теорема Виета)**:


$$\sum_{i=1}^n \lambda_i = \text{tr } A$$

$$\prod_{i=1}^n \lambda_i = \det A$$

Если матрица невырожденная ($\det A \neq 0$), то все её собственные значения ненулевые.

* **Лемма 1.** Для того, чтобы число $\lambda=0$ являлось собственным значением $A$, необх. и дост., чтобы $\det A = 0$.


* **Лемма 2.** Собственные значения матриц $A$ и $A^T$ совпадают.



Рассм. действительные матрицы, но комплексные векторы, т.к. собств. значения действ-х матриц могут быть комплексными.

**Пример:**

$$A = \begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix}$$

$$\det(\lambda I - A) = \begin{vmatrix} \lambda - 1 & -1 \\ 1 & \lambda - 1 \end{vmatrix} = 0$$

$$(\lambda - 1)^2 + 1 = 0 \Rightarrow (\lambda - 1)^2 = -1 \Rightarrow \lambda - 1 = \pm i \Rightarrow \lambda = 1 \pm i \in \mathbb{C}$$


Имеем $Ax = \lambda x$ (матрица $A \in \mathbb{R}$, вектор $x \in \mathbb{C}^n$, $\lambda \in \mathbb{C}$).

**Свойство 5)** $(Ax, y) = (x, A^T y)$ (док. для $\mathbb{R}^n$)
*Доказательство:*


$$(x, y) = \sum_{i=1}^n x_i y_i = [y_1, ..., y_n] \cdot \begin{bmatrix} x_1 \\ ... \\ x_n \end{bmatrix} = y^T x$$


Тогда:
$(Ax, y) = y^T (Ax)$
$(x, A^T y) = (A^T y)^T \cdot x = y^T A x$
Левые части равны, следовательно, свойство доказано $\blacksquare$.

В характеристическом многочлене $P(\lambda) = (\lambda - \lambda_1)(\lambda - \lambda_2)...(\lambda - \lambda_n) \equiv$


Пусть $\lambda_1, ..., \lambda_k$ — попарно различные собств. значения.
$\equiv (\lambda - \lambda_1)^{\alpha_1} \cdot (\lambda - \lambda_2)^{\alpha_2} \cdot ... \cdot (\lambda - \lambda_k)^{\alpha_k}$, где $\alpha_1 + \alpha_2 + ... + \alpha_k = n$.
$\alpha_i$ — кратность $\lambda_i$.

### Примеры нахождения собственных значений и векторов:

**1.** $I = \begin{bmatrix} 1 & 0 & ... & 0 \\ 0 & 1 & ... & 0 \\ ... & ... & ... & ... \\ 0 & 0 & ... & 1 \end{bmatrix}_{n \times n}$


$\det(\lambda I - I) = \det(I(\lambda - 1)) = \begin{bmatrix} \lambda-1 & & 0 \\ & ... & \\ 0 & & \lambda-1 \end{bmatrix} = (\lambda - 1)^n = 0 \Rightarrow \lambda = 1$


Собств. зн. $\lambda = 1$.
Собств. векторы $x$: $Ix = x$, т.е. $x - \forall \neq 0$ вектор.

**2.** $A = \begin{bmatrix} 1 & 1 & ... & 1 \\ 1 & 1 & ... & 1 \\ 1 & 1 & ... & 1 \end{bmatrix}_{n \times n}$

$$\det(\lambda I - A) = \lambda^n - n\lambda^{n-1} = \lambda^{n-1} (\lambda - n) = 0$$


Получаем:
$\lambda_1 = n$ (кратность 1)
$\lambda_2 = 0$ (кратность $n-1$)

*Найдём векторы:*
**2.1.** Для $\lambda_1 = n$:
$Ax = n x$


$$\begin{cases} x_1 + x_2 + ... + x_n = n x_1 \\ ... \\ x_1 + x_2 + ... + x_n = n x_n \end{cases} \Rightarrow x = e = \begin{bmatrix} 1 \\ ... \\ 1 \end{bmatrix}_{n \times 1}$$

**2.2.** Для $\lambda_2 = 0$:
$Ax = 0 \cdot x \Rightarrow Ax = 0$


$$\begin{cases} x_1 + x_2 + ... + x_n = 0 \\ ... \\ x_1 + x_2 + ... + x_n = 0 \end{cases}$$


Следовательно, любой вектор $x = \begin{bmatrix} x_1 \\ ... \\ x_n \end{bmatrix} \neq 0$, удовлетворяющий $\sum_{i=1}^n x_i = 0$, является собственным.

---

## Симметричные и положительно определённые матрицы



**Опр.** Матрица называется **симметричной**, если $A = A^T$; $A \in \mathbb{R}^{n \times n}$.

**Лемма.** Собственные значения симметричных матриц являются действительными числами.

**Теорема (Отношение Рэлея):**


Пусть $A \in \mathbb{R}^{n \times n}$ — симметричная матрица.
Тогда $\forall x \in \mathbb{R}^n; x \neq 0$:


$$\lambda_{min} \le \frac{(Ax, x)}{(x, x)} \le \lambda_{max}$$


где $\lambda_{min}$ и $\lambda_{max}$ — минимальное и максимальное из собств. значений $A$.
Более того:


$$\lambda_{min} = \min_{x \neq 0} \frac{(Ax, x)}{(x, x)}, \quad \lambda_{max} = \max_{x \neq 0} \frac{(Ax, x)}{(x, x)}$$


Дробь $\frac{(Ax, x)}{(x, x)}$ называется **отношением Рэлея**.

> 💡 **Объяснение:** Отношение Рэлея — это мощный инструмент для оценки собственных значений. Геометрически, если мы возьмём любой ненулевой вектор $x$, умножим его на матрицу $A$, и спроецируем результат обратно на $x$ (через скалярное произведение), а затем отнормируем, то полученное число *всегда* будет зажато между самым маленьким и самым большим собственным значением матрицы.

**Доказательство:**


Так как матрица симметричная, её собственные векторы $e_1, ..., e_n$ образуют ортонормированный базис: $(e_i, e_j) = \delta_{ij}$ (символ Кронекера). Разложим вектор $x$ по этому базису: $x = \sum \alpha_i e_i$.

Вычислим скалярные произведения:


$$(x, x) = \left(\sum_{i=1}^n \alpha_i e_i, \sum_{j=1}^n \alpha_j e_j\right) = \sum_{i=1}^n \sum_{j=1}^n \alpha_i \alpha_j (e_i, e_j) = \sum_{i=1}^n \alpha_i^2$$

$$(Ax, x) = \left(\sum_{i=1}^n \alpha_i \lambda_i e_i, \sum_{j=1}^n \alpha_j e_j\right) = \sum_{i=1}^n \sum_{j=1}^n \alpha_i \alpha_j \lambda_i (e_i, e_j) = \sum_{i=1}^n \lambda_i \alpha_i^2$$

Так как $\lambda_{min} \le \lambda_i \le \lambda_{max}$, оценим сумму:


$$\lambda_{min}(x, x) = \lambda_{min} \sum_{i=1}^n \alpha_i^2 \le (Ax, x) \le \lambda_{max} \sum_{i=1}^n \alpha_i^2 = \lambda_{max}(x, x)$$


Т.е., поделив на $(x,x) > 0$, получаем:


$$\lambda_{min} \le \frac{(Ax, x)}{(x, x)} \le \lambda_{max}$$

Покажем, что $\exists$ вектор, при котором достигается равенство. Подставим $x = e_1$ (вектор, соответствующий $\lambda_{min}$):


$$\frac{(Ae_1, e_1)}{(e_1, e_1)} = \frac{(\lambda_1 e_1, e_1)}{(e_1, e_1)} = \lambda_1 \frac{(e_1, e_1)}{(e_1, e_1)} = \lambda_1 = \lambda_{min}$$


Аналогично для $\lambda_{max}$, если подставить вектор, соответствующий $\lambda_{max}$. $\blacksquare$

**Опр.** Симметричная матрица $A$ называется **положительно определённой** и записывается $A > 0$, если $(Ax, x) > 0 \quad \forall x \neq 0 \in \mathbb{R}^n$.
**Положительно полуопределённой**, если $(Ax, x) \ge 0; \ A \ge 0 \quad \forall x \in \mathbb{R}^n$.

**Примеры:**
**1.** $A = \begin{bmatrix} 1 & 1 \\ 1 & 2 \end{bmatrix} \quad x = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \quad Ax = \begin{bmatrix} x_1 + x_2 \\ x_1 + 2x_2 \end{bmatrix}$

$$(Ax, x) = x_1(x_1 + x_2) + x_2(x_1 + 2x_2) = x_1^2 + 2x_1 x_2 + 2x_2^2 = (x_1 + x_2)^2 + x_2^2 > 0$$


Вывод: $A > 0$.

**2.** $A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} \quad x = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \quad Ax = \begin{bmatrix} x_1 + x_2 \\ x_1 + x_2 \end{bmatrix}$

$$(Ax, x) = x_1^2 + 2x_1 x_2 + x_2^2 = (x_1 + x_2)^2 \ge 0$$


Вывод: $A \ge 0$.
Если $A = 0 \Rightarrow x_1 = -x_2$, например $x = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$ или $x = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$ и т.д.

**Лемма.** Собственные значения положительно определённой матрицы положительны, а положительно полуопределённой — неотрицательны.


$$0 \le (Ax, x) = (\lambda x, x) = \lambda \underbrace{(x, x)}_{>0} \Rightarrow \lambda \ge 0$$

**Критерий Сильвестра:**


Для того, чтобы матрица $A$ была положительно определённой, необходимо и достаточно, чтобы все её угловые миноры были положительными.


$$A > 0 \quad ((Ax, x) > 0) \iff A \binom{1 \ 2 \ ... \ k}{1 \ 2 \ ... \ k} > 0 \quad \forall k = \overline{1, n}$$

**Для $A > 0$ справедливо:**

1. $\det A \neq 0$

2. диагональные элементы $a_{ii} > 0; \ i = \overline{1, n}$

3. $A^{-1} > 0$


**Опр.** Матрицы $A$ и $B$ **подобные**, если $\exists S; \det S \neq 0$:


$$A = S^{-1}BS \iff B = SAS^{-1}$$

 *(Примечание: в конспекте написано $A = S^{-1}BS \iff B = SAS^{-1}$, это стандартное определение подобия)*.

**Лемма.** Собственные значения подобных матриц совпадают.
*Доказательство:*


$$\det(\lambda I - A) = \det(\lambda I - S^{-1}BS) = \det(S^{-1}(\lambda I - B)S) = \det S^{-1} \cdot \det(\lambda I - B) \cdot \det S = \det(\lambda I - B)$$


Характеристические многочлены равны, значит их корни (собственные значения) совпадают.

---

## Нормы векторов и матриц



Рассм. $\mathbb{C}^n$.

**Опр.** Нормой вектора $x \in \mathbb{C}^n$ называется вещественное число:

1. $\vert{}\vert{}x\vert{}\vert{} \ge 0, \quad \vert{}\vert{}x\vert{}\vert{} = 0 \iff x = 0$

2. $\vert{}\vert{}\alpha x\vert{}\vert{} = \vert{}\alpha\vert{} \cdot \vert{}\vert{}x\vert{}\vert{}$

3. $\vert{}\vert{}x + y\vert{}\vert{} \le \vert{}\vert{}x\vert{}\vert{} + \vert{}\vert{}y\vert{}\vert{}$ (неравенство треугольника)



**Способы введения нормы в пространство:**

* **$l_\infty$ (кубическая):** $\vert{}\vert{}x\vert{}\vert{}_\infty \equiv \max_{1 \le i \le n} \vert{}x_i\vert{}$

* **$l_1$ (октаэдрическая):** $\vert{}\vert{}x\vert{}\vert{}_1 \equiv \sum_{i=1}^n \vert{}x_i\vert{}$

* **$l_2$ (сферическая/евклидова):** $\vert{}\vert{}x\vert{}\vert{}_2 \equiv \left( \sum_{i=1}^n \vert{}x_i\vert{}^2 \right)^{\frac{1}{2}}$


Это частные случаи **нормы Гёльдера $l_p$**:

$$\vert{}\vert{}x\vert{}\vert{}_p = \left( \sum_{i=1}^n \vert{}x_i\vert{}^p \right)^{\frac{1}{p}}; \quad p \ge 1$$

Оценим:


$$\max_{1 \le i \le n} \vert{}x_i\vert{} = \left( \max_{1 \le i \le n} \vert{}x_i\vert{}^p \right)^{\frac{1}{p}} \le \left( \sum_{i=1}^n \vert{}x_i\vert{}^p \right)^{\frac{1}{p}} \le \left( n \max_{1 \le i \le n} \vert{}x_i\vert{}^p \right)^{\frac{1}{p}} = n^{\frac{1}{p}} \max_{1 \le i \le n} \vert{}x_i\vert{}$$


При $p \to \infty \Rightarrow n^{1/p} \to 1$, следовательно $\left( \sum \vert{}x_i\vert{}^p \right)^{1/p} \to \max_{1 \le i \le n} \vert{}x_i\vert{} =: l_\infty$, поэтому и используется значок $\infty$.

Связь $l_2$ нормы со скалярным произведением:


$$\vert{}\vert{}x\vert{}\vert{}_2 = \left( \sum_{i=1}^n \vert{}x_i\vert{}^2 \right)^{\frac{1}{2}}$$

$$(x, x) = \sum_{i=1}^n \vert{}x_i\vert{}^2$$


Следовательно: $\vert{}\vert{}x\vert{}\vert{}_2 = \sqrt{(x, x)}$.

**Опр.** Нормой матрицы $A \in \mathbb{C}^{n \times n}$ называется вещественное число $\vert{}\vert{}A\vert{}\vert{}$:

1. $\vert{}\vert{}A\vert{}\vert{} \ge 0, \quad \vert{}\vert{}A\vert{}\vert{} = 0 \iff A = 0$

2. $\vert{}\vert{}\alpha A\vert{}\vert{} = \vert{}\alpha\vert{} \cdot \vert{}\vert{}A\vert{}\vert{}, \quad \forall \alpha \in \mathbb{C}$

3. $\vert{}\vert{}A + B\vert{}\vert{} \le \vert{}\vert{}A\vert{}\vert{} + \vert{}\vert{}B\vert{}\vert{}$