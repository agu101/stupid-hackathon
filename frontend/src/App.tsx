import { useRef, useState } from "react";
import SignatureCanvas from "react-signature-canvas";

function App() {
  const sigCanvas = useRef<SignatureCanvas>(null);
  const [trimmedDataURL, setTrimmedDataURL] = useState<string | null>(null);

  const sendImage = () => {
    if (sigCanvas.current != null) {
      setTrimmedDataURL(sigCanvas.current.getTrimmedCanvas().toDataURL("image/png"));
    }
    console.log(trimmedDataURL);
  };

  return (
    <>
      <h1>Draw a number</h1>
      <div>
        <SignatureCanvas
          ref={sigCanvas}
          canvasProps={{ width: 500, height: 200, className: "sigCanvas" }}
          backgroundColor="#D3D3D3"
        />
      </div>
      <div>
        <button onClick={sendImage}>Send</button>
      </div>
      <h2>Image</h2>
      {trimmedDataURL ? <img alt="signature" src={trimmedDataURL} /> : null}
    </>
  );
}

export default App;
