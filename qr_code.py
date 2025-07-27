import streamlit as st
import qrcode
from PIL import Image
import io

# Streamlit App Title
st.title("🔳 QR Code Generator")

# User Input
text_input = st.text_input("Enter text or URL to generate QR code:")

# Button to generate QR
if st.button("Generate QR Code"):
    if text_input.strip() == "":
        st.warning("⚠️ Please enter some text to generate a QR code.")
    else:
        # Generate QR Code
        qr = qrcode.make(text_input)

        # Convert to BytesIO
        buf = io.BytesIO()
        qr.save(buf, format="PNG")
        buf.seek(0)

        # Show QR Code in Streamlit
        st.image(buf, caption="Live QR Code Preview", use_container_width=False)

        # Download button
        st.download_button(
            label="📥 Download QR Code",
            data=buf,
            file_name="qr_code.png",
            mime="image/png"
        )
