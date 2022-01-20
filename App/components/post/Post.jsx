import "./post.css";
import { MoreVert } from "@material-ui/icons";
import { useState } from "react";

export default function Post({ post }) {
    const [like, setLike] = useState(post.like)
    const [isLiked, setIsLiked] = useState(false)


    return (
        <div className="post">
            <div className="postWrapper">
              test1
            </div>
        </div>
    );
}