import styles from "@/styles/Cipher.module.scss";
import { availableKeyType } from "@/utils/type";

export default function Key({ type }: { type: availableKeyType }) {
  if (type == "Text") {
    return (
      <>
        <label htmlFor="Key">Key</label>
        <textarea
          name="Key"
          className={`${styles.input} ${styles.key}`}
          placeholder="Please input the key here..."
        />
      </>
    );
  }

  return (
    <>
      <label htmlFor="Key">Key</label>
      <div className={styles["key-wrapper"]}>
        <div className={styles["label-container"]}>
          <label htmlFor="M">M</label>
          <input name="M" className={`${styles.affine}`} placeholder="7" />
        </div>
        <div className={styles["label-container"]}>
          <label htmlFor="B">B</label>
          <input name="B" className={`${styles.affine}`} placeholder="6" />
        </div>
      </div>
    </>
  );
}
