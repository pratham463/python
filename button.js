< !DOCTYPE html >
    <html lang="en">
        <head>
            <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Change Background Color</title>
                    <style>
                        body {
                            text - align: center;
                        padding: 50px;
    }
                        button {
                            padding: 10px 20px;
                        font-size: 16px;
                        cursor: pointer;
    }
                    </style>
                </head>
                <body>
                    <h1>Click the Button to Change Background Color</h1>
                    <button id="colorButton">Change Background</button>

                    <script>
                        const button = document.getElementById('colorButton');
    button.addEventListener('click', () => {
      // Generate a random color
      const randomColor = `#${Math.floor(Math.random() * 16777215).toString(16)}`;
                        document.body.style.backgroundColor = randomColor;
    });
                    </script>
                </body>
            </html>
            How it works:
            HTML: A button is created with the ID colorButton.
            CSS: Basic styling is applied for better visuals.
            JavaScript:
            An event listener is added to the button.
            When clicked, it generates a random color using Math.random() and applies it to the backgroundColor of the body.
            Feel free to customize the colors or add more functionality!

