"use client";

import styles from "@/styles/Cipher.module.scss";
import { description } from "@/utils/desc";
import { Inter } from "@next/font/google";
const inter = Inter({ subsets: ["latin"] });
export default function Home() {
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
            <label htmlFor="Key">key</label>
            <textarea name="Key" className={styles.input} />
            <label htmlFor="result">decrypt</label>
            <textarea name="result" className={styles.input} />
          </form>
          <div className={styles.btn_container}>
            <button type="submit" className={styles.btn}>
              <a href="favicon.ico" download="result.txt">
                Download file
              </a>
            </button>
            <label htmlFor="file">Upload File</label>
            <input type="file" name="file" />
            <button type="button" className={styles.btn}>
              Encrypt plaintext
            </button>
            <button type="button" className={styles.btn}>
              Decrypt ciphertext
            </button>
            <button type="button" className={styles.btn}>
              Clear
            </button>
          </div>
        </div>
      </div>
    </main>
  );
}
