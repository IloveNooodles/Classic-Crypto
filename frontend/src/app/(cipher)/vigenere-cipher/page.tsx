"use client";

import { description } from "@/utils/desc";
import { Inter } from "@next/font/google";
import styles from "./page.module.css";
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
            <label htmlFor="encrypt">Encrypt</label>
            <textarea name="encrypt" className={styles.input} />
            <label htmlFor="decrypt">decrypt</label>
            <textarea name="decrypt" className={styles.input} />
            <label htmlFor="key">key</label>
            <textarea name="key" className={styles.input} />
          </form>
          <div className={styles.btn_container}>
            <button type="submit">
              <a href="favicon.ico" download="result.txt">
                Download file
              </a>
            </button>
            <label htmlFor="file">Upload File</label>
            <input type="file" name="file" />
            <button type="button">Encrypt plaintext</button>
            <button type="button">Decrypt ciphertext</button>
            <button type="button">Clear</button>
          </div>
        </div>
      </div>
    </main>
  );
}
