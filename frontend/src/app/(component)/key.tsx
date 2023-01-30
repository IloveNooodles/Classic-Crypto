import styles from "@/styles/Cipher.module.scss";
import { availableKeyType } from "@/utils/type";
import { Dispatch, SetStateAction } from "react";

export default function Key({
  type,
  cipherKey,
  setKey,
}: {
  type: availableKeyType;
  cipherKey: any;
  setKey: Dispatch<SetStateAction<{}>>;
}) {
  if (type == "Text") {
    return (
      <>
        <label htmlFor="key">Key</label>
        <textarea
          name="key"
          className={`${styles.input} ${styles.key}`}
          placeholder="Please input the key here..."
          onChange={(e) => {
            setKey({ ...cipherKey, text: e.target.value });
          }}
        />
      </>
    );
  }

  return (
    <>
      <label htmlFor="Key">Key</label>
      <div className={styles["key-wrapper"]}>
        <div className={styles["label-container"]}>
          <label htmlFor="m">M</label>
          <input
            name="m"
            className={`${styles.affine}`}
            placeholder="7"
            onChange={(e) => {
              setKey({ ...cipherKey, m: e.target.value });
            }}
          />
        </div>
        <div className={styles["label-container"]}>
          <label htmlFor="b">B</label>
          <input
            name="b"
            className={`${styles.affine}`}
            placeholder="6"
            onChange={(e) => {
              setKey({ ...cipherKey, b: e.target.value });
            }}
          />
        </div>
      </div>
    </>
  );
}
