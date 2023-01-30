import styles from "@/styles/Cipher.module.scss";
import { BASE_URL } from "@/utils/desc";
import { RootForm } from "@/utils/type";
import { faUpload } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { ChangeEvent, useRef, useState } from "react";

export default function ButtonGroup({ ...props }: RootForm) {
  const fileRef = useRef<HTMLInputElement>(null);
  const infoRef = useRef<HTMLParagraphElement>(null);
  const [File, setFile] = useState<File | null>(null);
  const { cipherKey, text, url, result } = props;

  async function handleSubmit(isEncrypt: boolean) {
    let body = new FormData();
    if (File) {
      body.append("file", File);
    }
    body.append("key", cipherKey?.text?.toUpperCase() || "");
    body.append("b", cipherKey?.b?.toUpperCase() || "");
    body.append("m", cipherKey?.m?.toUpperCase() || "");
    body.append("text", text?.current?.value.toUpperCase() || "");
    if (isEncrypt) {
      body.append("encrypt", "true");
    } else {
      body.append("encrypt", "false");
    }

    console.log(File, cipherKey, text?.current?.value);

    const data = await fetch(BASE_URL + url, {
      method: "POST",
      body: body,
    });
    const res = await data.json();
    console.log(res.Result);
    if (result) result.current!.value = res.Result;
  }

  return (
    <>
      <div className={styles["btn-container"]}>
        {!File && (
          <div
            className={styles["file-upload"]}
            onClick={() => {
              if (!fileRef.current) return;
              fileRef.current.click();
            }}
          >
            <p>Upload File</p>
            <FontAwesomeIcon icon={faUpload} size="2x" />
            <input
              type="file"
              name="file"
              id="file"
              hidden
              ref={fileRef}
              onChange={(event: ChangeEvent<HTMLInputElement>) => {
                event.preventDefault();
                let file = event.target.files;
                if (!file) return;
                if (!infoRef.current) return;
                infoRef.current.textContent = file[0].name;
                setFile(file[0]);
              }}
            />
          </div>
        )}
        <div
          className={styles["file-upload"]}
          style={File ? { display: "block" } : { display: "none" }}
        >
          <p>File uploaded!</p>
          <p ref={infoRef}>File uploaded!</p>
        </div>
        <button
          type="reset"
          className={styles.btn}
          onClick={() => {
            setFile(null);
          }}
        >
          Clear
        </button>
        <button type="button" className={styles.btn}>
          <a href="http://127.0.0.1:5000/static/a.txt" download="result.txt">
            Download file
          </a>
        </button>
        <button
          type="submit"
          className={styles.btn}
          onClick={(e) => {
            e.preventDefault();
            handleSubmit(true);
          }}
        >
          Encrypt plaintext
        </button>
        <button
          type="submit"
          className={styles.btn}
          onClick={(e) => {
            e.preventDefault();
            handleSubmit(false);
          }}
        >
          Decrypt ciphertext
        </button>
      </div>
    </>
  );
}
