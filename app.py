import streamlit as st
from database import get_all_products, create_product, update_product, delete_product

st.title("Aplikasi CRUD dengan Streamlit")

menu = ["Create", "Read", "Update", "Delete"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Create":
    st.subheader("Menambah Produk Baru")
    name = st.text_input("Nama Produk")
    price = st.number_input("Harga", min_value=0.0, format="%.2f")
    description = st.text_area("Deskripsi")

    if st.button("Tambah Produk"):
        create_product(name, price, description)
        st.success("Produk berhasil ditambahkan!")

elif choice == "Read":
    st.subheader("Daftar Produk")
    products = get_all_products()
    for product in products:
        st.write(f"ID: {product.id}")
        st.write(f"Nama: {product.name}")
        st.write(f"Harga: {product.price}")
        st.write(f"Deskripsi: {product.description}")
        st.write("-----------")

elif choice == "Update":
    st.subheader("Update Produk")
    product_id = st.number_input("ID Produk", min_value=1, step=1)
    name = st.text_input("Nama Produk Baru")
    price = st.number_input("Harga Baru", min_value=0.0, format="%.2f")
    description = st.text_area("Deskripsi Baru")

    if st.button("Update Produk"):
        update_product(product_id, name, price, description)
        st.success("Produk berhasil diperbarui!")

elif choice == "Delete":
    st.subheader("Hapus Produk")
    product_id = st.number_input("ID Produk untuk Dihapus", min_value=1, step=1)

    if st.button("Hapus Produk"):
        delete_product(product_id)
        st.success("Produk berhasil dihapus!")
