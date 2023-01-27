"use client";

import styles from "@/styles/Cipher.module.scss";
import { description } from "@/utils/desc";
import { faUpload } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { Inter } from "@next/font/google";
import { ChangeEvent, useRef, useState } from "react";
const inter = Inter({ subsets: ["latin"] });
export default function Home() {
  const fileRef = useRef<HTMLInputElement>(null);
  const infoRef = useRef<HTMLParagraphElement>(null);
  const [File, setFile] = useState<File | null>(null);

  return (
    <main className={styles.main}>
      <div className={styles.center}>
        <div className={styles.description}>
          <code className={styles.title}>Vigenere Cipher</code>
          <p className={inter.className}>{description[0]}</p>
        </div>
        <div className={styles.container}>
          <form className={styles.form}>
            <label htmlFor="input">Input</label>
            <textarea name="input" className={styles.input} />
            <label htmlFor="Key">Key</label>
            <textarea name="Key" className={`${styles.input} ${styles.key}`} />
            <label htmlFor="result">Result</label>
            <textarea name="result" className={styles.input} />
            <input type="hidden" name="vignere" />
          </form>
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
        </div>
      </div>
    </main>
  );
}
