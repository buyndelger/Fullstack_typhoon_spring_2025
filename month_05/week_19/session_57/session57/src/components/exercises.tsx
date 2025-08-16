import React, { useEffect, useState } from "react";

interface Post {
    id: number;
    title: string;
    body: string;
}


export const FetchList: React.FC = () => {
    const [posts, setPosts] = useState<Post[]>([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchPosts = async () => {
            try {
                const res = await fetch("https://jsonplaceholder.typicode.com/posts");
                const data: Post[] = await res.json();
                setPosts(data.slice(0, 10));
            } catch (err) {
                console.error(err);
            } finally {
                setLoading(false);
            }
        };
        fetchPosts();
    }, []);

    if (loading) return <p>Loading posts...</p>;

    return (
        <div>
            <h2>EX01 - Fetch List</h2>
            <ul>
                {posts.map((post) => (
                    <li key={post.id}>
                        <h3>
                            {post.id}. {post.title}
                        </h3>
                        <p>{post.body}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};


export const RefreshRandomPost: React.FC = () => {
    const [post, setPost] = useState<Post | null>(null);

    const fetchRandomPost = async () => {
        const randomId = Math.floor(Math.random() * 100) + 1;
        try {
            const res = await fetch(
                `https://jsonplaceholder.typicode.com/posts/${randomId}`
            );
            const data: Post = await res.json();
            setPost(data);
        } catch (err) {
            console.error(err);
        }
    };

    useEffect(() => {
        fetchRandomPost();
    }, []);

    return (
        <div>
            <h2>EX02 - Refresh Random Post</h2>
            <button onClick={fetchRandomPost}>Get New Random Post</button>
            {post && (
                <div>
                    <h3>
                        {post.id}. {post.title}
                    </h3>
                    <p>{post.body}</p>
                </div>
            )}
        </div>
    );
};


export const FetchBasedOnUserInput: React.FC = () => {
    const [inputId, setInputId] = useState<string>("");
    const [post, setPost] = useState<Post | null>(null);

    useEffect(() => {
        if (!inputId) {
            setPost(null);
            return;
        }

        const timeout = setTimeout(async () => {
            try {
                const res = await fetch(
                    `https://jsonplaceholder.typicode.com/posts/${inputId}`
                );
                const data: Post = await res.json();
                setPost(data);
            } catch (err) {
                console.error(err);
            }
        }, 500);

        return () => clearTimeout(timeout);
    }, [inputId]);

    return (
        <div>
            <h2>EX03 - Fetch Based On User Input</h2>
            <input
                type="number"
                value={inputId}
                onChange={(e) => setInputId(e.target.value)}
                placeholder="1-100 хооронд ID оруулна уу"
            />
            {post && (
                <div>
                    <h3>
                        {post.id}. {post.title}
                    </h3>
                    <p>{post.body}</p>
                </div>
            )}
        </div>
    );
};
