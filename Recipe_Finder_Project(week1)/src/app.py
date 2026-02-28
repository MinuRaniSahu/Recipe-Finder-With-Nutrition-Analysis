if dish:
    result = DevSearch_expedition(dish)

    if isinstance(result, dict):
        st.subheader("Ingredients")
        for item in result["Ingredients"]:
            st.write("- " + item)

        st.subheader("Instructions")
        st.write(result["Instructions"])
    else:
        st.write(result)
