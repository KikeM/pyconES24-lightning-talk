import marimo

__generated_with = "0.9.1"
app = marimo.App(app_title="Bicycle Integral")


@app.cell
def __():
    import sympy as sp
    import marimo as mo
    import matplotlib.pyplot as plt
    return mo, plt, sp


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        # Una Integral Elegante Escondida En Una Bicicleta


        ---
        """
    )
    return


@app.cell
def __():
    return


@app.cell
def __():
    return


@app.cell
def __():
    return


@app.cell
def __():
    return


@app.cell
def __():
    return


@app.cell
def __():
    return


@app.cell(hide_code=True)
def __(mo):
    mo.image("/Users/valbuena/git/github.com/pycones24-lightning-talk/diagram.png", height=500, rounded=True)
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## Estrategia

        1. **No-deslizamiento** 
        1. Construir un **triángulo**
        1. Encontrar el centro instantáneo de rotación  (CIR).

        ### **CIR + punto velocidad conocida = velocidad angular**.

        ¡Empezamos!
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.image("/Users/valbuena/git/github.com/pycones24-lightning-talk/diagram-cropped.png", height=400)
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## Cálculo de $\phi(t)$
        La altura $H(\phi)$ es la suma de dos lados de cada triángulo, $p(\phi)$ y $q(\phi)$,

        $$
        \begin{align}
        H(\phi) &= p(\phi) + q(\phi) \\
        H(\phi) &=  \sin{\left(\phi \right)} \tan{\left(\phi \right)} + \cos{\left(\phi \right)}
        \end{align}
        $$

        Conocido $H(\phi)$, tenemos una ecuación diferencial para hallar $\phi(t)$:

        $$
        \begin{align}
        H(\phi) \frac{d\phi}{dt} &= v_0 \\
        \int \left(\sin{\left(\phi \right)} \tan{\left(\phi \right)} + \cos{\left(\phi \right)}\right) d\phi &= v_0 t + C 
        \end{align}
        $$
        """
    )
    return


@app.cell
def __(sp):
    phi, t, x, y = sp.symbols("phi, t, x, y")
    return phi, t, x, y


@app.cell
def __(phi, sp, t):
    xM = t - sp.sin(phi)
    yM = sp.cos(phi)
    return xM, yM


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        Con SymPy, podemos obtener la primitiva de esta función:

        $$
        \int \left(\sin{\left(\phi \right)} \tan{\left(\phi \right)} + \cos{\left(\phi \right)}\right) d\phi
        = 
        \frac{1}{2}\ln{\left(\frac{\sin{\left(\phi \right)} + 1}{\sin{\left(\phi \right)} - 1} \right)}
        $$
        """
    )
    return


@app.cell(hide_code=True)
def __(phi, sp):
    p_phi = sp.sin(phi) * sp.tan(phi)
    q_phi = sp.cos(phi)
    H_phi = p_phi + q_phi

    primitive = sp.logcombine(sp.integrate(H_phi), force=True)
    primitive
    return H_phi, p_phi, primitive, q_phi


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""**Nota:** han sido mejores los resultados de SymPy que de WolframAlpha.""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.image("/Users/valbuena/git/github.com/pycones24-lightning-talk/wolfram-alpha.png", height=300)
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        Nos queda un último paso, despejar $\phi(t)$:

        $$
        \begin{align}
        \frac{1}{2}\ln{\left(\frac{\sin{\left(\phi \right)} + 1}{\sin{\left(\phi \right)} - 1} \right)} &= t
        \\[5mm]
        \phi(t) &= \sin^{-1}{\left(\tanh{\left(t \right)} \right)}
        \end{align}
        $$
        """
    )
    return


@app.cell
def __(phi, sp, t):
    solutions = sp.solve((1+sp.sin(phi))/(1-sp.sin(phi))-sp.exp(2*t),phi)
    return (solutions,)


@app.cell
def __(solutions):
    solutions
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""SymPy nos da **dos** soluciones, las **cuestiones con ángulos** a menudo tienen **solución** pero no **unicidad**.""")
    return


@app.cell(hide_code=True)
def __(solutions, sp, t):
    phi_time = solutions[1]
    sp.plot(phi_time, sp.pi/2,(t, 0, 8), title="Bicycle angle $\phi$ in time", xlabel="Time", ylabel="$\phi [rad]$", size=(7,3))
    return (phi_time,)


@app.cell(hide_code=True)
def __(phi, phi_time, sp, t, xM, yM):
    xM_time = xM.subs(phi, phi_time)
    yM_time = yM.subs(phi, phi_time)

    sp.plot_parametric(xM_time, yM_time, (t, 0, 8), title = "Trajectory of the rear tyre", xlabel="Time", ylabel= "Movement of Point M", size=(7,3))
    return xM_time, yM_time


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ### Ecuaciones originales (dos parámetros no independientes)

        $$
        \begin{align}
        x_M &= t - \sin(\phi)
        \\
        y_M &= \cos(\phi)
        \end{align}
        $$

        ### Ecuaciones paramétricas 

        $$
        \begin{align}
        x_M &= t - \tanh(t)
        \\
        y_M &= \sqrt{1-\tanh^2(t)}
        \end{align}
        $$
        """
    )
    return


if __name__ == "__main__":
    app.run()
