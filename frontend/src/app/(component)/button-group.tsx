import styles from "@/styles/Cipher.module.scss";
import { faUpload } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { ChangeEvent, useRef, useState } from "react";

export default function ButtonGroup() {
  const fileRef = useRef<HTMLInputElement>(null);
  const infoRef = useRef<HTMLParagraphElement>(null);
  const [File, setFile] = useState<File | null>(null);
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

        <button type="submit" className={styles.btn}>
          <a href="favicon.ico" download="result.txt">
            Download file
          </a>
        </button>
        <button type="submit" className={styles.btn}>
          Encrypt plaintext
        </button>
        <button type="submit" className={styles.btn}>
          Decrypt ciphertext
        </button>
        <button type="submit" className={styles.btn}>
          Clear
        </button>
      </div>
    </>
  );
}
