import { useState } from "react";

export default function Home() {
  const [text, setText] = useState("");
  const [data, setData] = useState<any>(null);

  const generate = async () => {
    const res = await fetch(process.env.NEXT_PUBLIC_API_URL + "/generate", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ text })
    });

    setData(await res.json());
  };

  const getSimilar = async (i:number) => {
    const res = await fetch(process.env.NEXT_PUBLIC_API_URL + "/similar/" + i);
    alert("Similar index: " + JSON.stringify(await res.json()));
  };

  return (
    <div style={{padding:40}}>
      <h1>Patent AI</h1>

      <textarea onChange={e=>setText(e.target.value)} />
      <br/><br/>
      <button onClick={generate}>Generate</button>

      {data && (
        <>
          <h2>Count: {data.count}</h2>

          <h2>Keywords</h2>
          <pre>{JSON.stringify(data.keywords,null,2)}</pre>

          <h2>Patents (click for similar)</h2>
          {data.patents.map((p:any,i:number)=>(
            <div key={i} onClick={()=>getSimilar(i)} style={{cursor:"pointer"}}>
              {p.title} - {p.assignee}
            </div>
          ))}

          <h2>WordCloud</h2>
          <img src={process.env.NEXT_PUBLIC_API_URL+"/wordcloud?t="+Date.now()} />

          <h2>TF-IDF</h2>
          <img src={process.env.NEXT_PUBLIC_API_URL+"/tfidf?t="+Date.now()} />
        </>
      )}
    </div>
  );
          }
