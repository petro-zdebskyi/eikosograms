import matplotlib.pyplot as plt
import matplotlib.patheffects as pe

_THEME_COLORS = {
    'color': {
        'drk_l': 'tab:blue',
        'drk_r': 'tab:orange',
        'lgt_l': 'lightsteelblue',
        'lgt_r': 'wheat'
    },
    'blue': {
        'drk_l': 'tab:blue',
        'drk_r': 'tab:blue',
        'lgt_l': 'whitesmoke',
        'lgt_r': 'whitesmoke'
    },
    'contrast': {
        'drk_l': 'blue',
        'drk_r': 'black',
        'lgt_l': 'lightgrey',
        'lgt_r': 'lightgrey'
    }
}

def draw_chart(
        b_a,
        b_not_a,
        a,
        names=('A', 'B'), 
        theme='color', 
        show_proba=True, 
        min_labels=True
    ):
    """
    Draw eikosogram for 2 binary variables and calculate P(A | B).

    P(A | B) = P(B|A)*P(A) / P(B)
    P(A | B) = P(B|A)*P(A) / (P(B|A)*P(A) + P(B|notA)*P(notA))

    Parameters
    ----------
    b_a : float
        P(B | A).
    b_not_a : float
        P(B | not A).
    a : float
        P(A).
    names : (str, str)
        Names of two binary variables.
    theme : {'color', 'contrast', 'blue'}, default: 'color'
        Defines colors used in chart.
    show_proba : bool, default: True
        Show box with conditional probability P(A | B).
    min_labels : bool, default: True
        Minimalistic labels for input parameters with only a number.
    
    Returns
    -------
    None

    Examples
    --------
    >>> draw_chart(.8, .3, .4, names=('Rain', 'Cloudy'), min_labels=False)
    """

    e1, e2 = names

    c = [_THEME_COLORS[theme]['lgt_l'], _THEME_COLORS[theme]['lgt_r']]
    plt.bar([a/2, (1-a)/2+a], height=1, width=[a, 1-a], color=c)

    c = [_THEME_COLORS[theme]['drk_l'], _THEME_COLORS[theme]['drk_r']]
    plt.bar([a/2, (1-a)/2+a], height=[b_a, b_not_a], width=[a, 1-a], color=c)

    # outline
    plt.axis('off')
    plt.plot([0, 0], [0, 1], c='k', lw=.7)
    plt.plot([0, 1], [1, 1], c='k', lw=.7)
    plt.plot([1, 1], [1, 0], c='k', lw=.7)
    plt.plot([0, 1], [0, 0], c='k', lw=.7)
    plt.plot([a, a], [0, 1], c='k', lw=.7)
    plt.plot([0, a], [b_a, b_a], c='k', lw=.7)
    plt.plot([a, 1], [b_not_a, b_not_a], c='k', lw=.7)
    plt.ylim([-.01, 1])

    # name labels
    plt.text(
        a/2, -.01, e1,
        horizontalalignment='center', verticalalignment='top', 
    )
    plt.text(
        (1-a)/2+a, -.01, f'not {e1}',
        horizontalalignment='center', verticalalignment='top', 
    )
    plt.text(
        -.01, b_a/2, e2, 
        horizontalalignment='right', verticalalignment='center', 
    )
    plt.text(
        -.01, (1-b_a)/2+b_a, f'not {e2}', 
        horizontalalignment='right', verticalalignment='center', 
    )
    
    # number labels 
    plt.text(
        a/2, b_a+.005, b_a if min_labels else f'P({e2} | {e1}) = {b_a}', 
        horizontalalignment='center', verticalalignment='bottom',
        path_effects=[pe.withStroke(linewidth=2, foreground='white')]
    )
    plt.text(
        (1-a)/2+a, b_not_a+.005, 
        b_not_a if min_labels else f'P({e2} | not {e1}) = {b_not_a}',  
        horizontalalignment='center', verticalalignment='bottom', 
        path_effects=[pe.withStroke(linewidth=2, foreground='white')]
    )
    plt.text(
        a-.005, .5, a if min_labels else f'P({e1}) = {a}', rotation=90,
        horizontalalignment='right', verticalalignment='center', 
        path_effects=[pe.withStroke(linewidth=2, foreground='white')]
    )

    # conditional probability box
    if show_proba:
        a_b = b_a*a / (b_a*a + b_not_a*(1-a))  # Bayes' theorem, P(A | B)
        label_text = f'P({e1} | {e2}) = {a_b:.2f}'
        plt.text(
            .5+.005, 1.05-.005, label_text, 
            size=10, horizontalalignment='center', 
            bbox=dict(facecolor='k', edgecolor='k', boxstyle='round')
        )  # shadow
        plt.text(
            .5, 1.05, label_text, 
            size=10, horizontalalignment='center', 
            bbox=dict(facecolor='white', edgecolor='k', boxstyle='round')
        )
    
    plt.show()
