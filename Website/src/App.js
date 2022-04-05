import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from 'react-router-dom';
import FileUpload from './components/fileUpload';
import InfoCard from './components/infoCard';
import List from './components/list';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/info-card" element={<InfoCard />} />
        <Route path="/list" element={<List />} />
        <Route path="/home" element={<FileUpload />} />
        <Route path="/" element={<Navigate replace to="/home" />} />
      </Routes>
    </Router>
  );
}

export default App;
