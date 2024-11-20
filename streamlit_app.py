<form id="upload-form">
    <input type="file" id="file-input" name="file">
    <button type="submit">Detect Tumor</button>
</form>
<div id="result"></div>

<script>
    document.getElementById('upload-form').onsubmit = async (e) => {
        e.preventDefault();
        let fileInput = document.getElementById('file-input');
        let formData = new FormData();
        formData.append('file', fileInput.files[0]);

        let response = await fetch('/predict', { method: 'POST', body: formData });
        let result = await response.json();
        document.getElementById('result').innerText = 'Result: ' + result.prediction;
    };
</script>
