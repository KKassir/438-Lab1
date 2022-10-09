import React, {useState, useEffect} from "react";
import './App.css';
import Axios from 'axios';

function App() {
  const [movieName, setMovieName]= useState("");
  const [review, setReview]= useState("");
  const [movieReviewList, setMovieList]=useState([]);
  const [DesiredMovie, setDesiredMovie] = useState("");
  const [Result, setResult] = useState({});
  const [newReview, setNewReview]= useState("");
  useEffect(()=>{
    Axios.get("http://localhost:3001/api/get").then((response) => {
      setMovieList(response.data.sort((a,b) => (a.movieName > b.movieName) ? 1 : -1));
	// The movies will be sorted according to alphabetical order (After page is refreshed).
    });
  },[]);


  const submitReview=()=>{

    Axios.post("http://localhost:3001/api/insert", {
      movieName: movieName,
      movieReview: review,
    });

      setMovieList([
        ...movieReviewList,
        { movieName: movieName, movieReview: review },
      ]);
 };
	// Search For Movie

   const MovieSearch = () => {
    for (let i=0 ; i<movieReviewList.length;i++) {
      if (movieReviewList[i].movieName === DesiredMovie) {
        setResult(movieReviewList[i]);
        return;
      }
    };
   };



 const deleteReview = (movie) => {
   Axios.delete(`http://localhost:3001/api/delete/${movie}`);
 };

 const updateReview = (movie) => {
   Axios.put("http://localhost:3001/api/update", {
     movieName: movie,
     movieReview: newReview,
   });
   setNewReview("")
 };

  return (
    <div className="App"><h1>CRUD APPLICATION </h1>
    <div className="form">
   
    <h2> Add a new movie</h2>
    <div className="form">
    <label>Movie Name:</label>
    <input type="text" name="movieName" onChange={(e)=>{
      setMovieName(e.target.value)
    }}/>
    <label>Review:</label>
    <input type="text" name="Review" onChange={(e)=>{
      setReview(e.target.value)
    }}/>


    <button onClick={submitReview}> Submit </button>



  <label>
        Search for your movie
      </label>
      <input type="text" name="DesiredMovie" onChange={(e)=>{
        setDesiredMovie(e.target.value)
      }}/>
    
      <button onClick = {MovieSearch}> Search </button>
    </div>
   
    {Result.movieName != null && 
        <div className="card">
          <h1> {Result.movieName} </h1>
          <p> {Result.movieReview} </p>
        </div>
      
    }

    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>




    {movieReviewList.map((val)=>{
      return (
        <div className="card">
          <h1> {val.movieName} </h1>
          <p> {val.movieReview} </p>

          <button onClick={() => {deleteReview(val.movieName)}}>Delete</button>
          <input type="text" id="updateInput" onChange={(e) => {setNewReview(e.target.value)}}/>
          <button onClick={()=> {updateReview(val.movieName)}}>Update</button>
        </div>
      );
    })}
  </div>
</div>
);
}

export default App;

