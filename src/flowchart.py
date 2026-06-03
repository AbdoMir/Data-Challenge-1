from graphviz import Digraph


def make_consort_flowchart(
    N_screened: int,
    N_excluded: int,
    N_randomized: int,
    N_bup: int,
    N_clon: int,
    N_abandon: int,
    output_path: str = "outputs/figures/flowchart_consort"
):
    """
    Génère un flowchart CONSORT automatiquement.

    Parameters
    ----------
    N_screened : int
        Nombre de patients évalués
    N_excluded : int
        Nombre de patients exclus
    N_randomized : int
        Nombre de patients randomisés
    N_bup : int
        Nombre assignés au bras BUPNAL
    N_clon : int
        Nombre assignés au bras CLON
    N_abandon : int
        Nombre d'abandons précoces
    output_path : str
        Chemin de sortie sans extension
    """

    N_PP = N_randomized - N_abandon

    dot = Digraph(
        comment="CONSORT Flow Diagram",
        format="png"
    )

    dot.attr(rankdir="TB", fontsize="10")

    # Nœuds
    dot.node("A", f"Patients évalués\nN = {N_screened}")
    dot.node("B", f"Exclus\nN = {N_excluded}")
    dot.node("C", f"Randomisés\nN = {N_randomized}")

    dot.node("D", f"Affectés BUPNAL\nN = {N_bup}")
    dot.node("E", f"Affectés CLON\nN = {N_clon}")

    dot.node("F", f"Abandons précoces\nN = {N_abandon}")
    dot.node("G", f"Analysés per-protocol\nN = {N_PP}")

    # Liens
    dot.edge("A", "B")
    dot.edge("A", "C")
    dot.edge("C", "D")
    dot.edge("C", "E")
    dot.edge("D", "F")
    dot.edge("E", "F")
    dot.edge("F", "G")

    # Export
    dot.render(output_path, cleanup=True)

    return dot
