"use client";
import styles from './page.module.css'
import Chat from '../pages/chat';

export default function Home() {
  return (
    <main className={styles.main}>
      <Chat />
    </main>
  )
}
