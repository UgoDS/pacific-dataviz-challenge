def align_subheader(st, txt: str):
    return st.markdown(
        f"<h2 style='text-align: center; color: black;'>{txt}</h2>",
        unsafe_allow_html=True,
    )


def align_caption(st, txt: str):
    return st.markdown(
        f"<p style='text-align: center; color: grey;'>{txt}</p>",
        unsafe_allow_html=True,
    )
