import React from 'react';

class BookInfo extends React.Component {
    render() {
        const tdStyleISBN = {
            width: '20%',
            border: '1px solid',
            padding: '3px 13px',
        };
        
        const tdStyle = {
            width: '50%',
            border: '1px solid',
            padding: '3px 13px',
        };

        return (
            <tr>
                <td style={tdStyleISBN}>{this.props.book.isbn}</td>
                <td style={tdStyle}>{this.props.book.title}</td>
                <td style={tdStyle}>{this.props.book.publisher}</td>
                <td style={tdStyle}>{this.props.book.year_published}</td>
                <td style={tdStyle}>{this.props.book.genre}</td>
            </tr>
        )
    }
}

class BookList extends React.Component {
    render() {
        const booklist = this.props.books.map(
            book => <BookInfo key={book.isbn} book={book} />
        );

        const tableStyle = { width: '90%' };
        const thStyle = {
            width: '50%',
            border: '1px solid',
            padding: '7px'
        };

        return (
            <center>
                <table style={tableStyle}>
                    <tbody>
                        <tr>
                            <th style={thStyle}>ISBN</th>
                            <th style={thStyle}>Title</th>
                            <th style={thStyle}>Publisher</th>
                            <th style={thStyle}>Year</th>
                            <th style={thStyle}>Genre</th>
                        </tr>
                        {booklist}
                    </tbody>
                </table>
            </center>
        )
    }
}

export default BookList;